#pragma once
#include <cassert>

#include "utils.hpp"

namespace ioh::common
{
    static int get_next_id(const std::vector<int>& ids)
    {
        return ids.empty() ? 1 : (*std::max_element(ids.begin(), ids.end())) + 1;
    }

    template <class AbstractType, typename ...Args>
    struct Factory
    {
        using Type = std::shared_ptr<AbstractType>;
        using Creator = std::function<Type(Args &&...)>;

        static Factory &instance()
        {
            static Factory f; // NOLINT 
            return f;
        }

        void include(const std::string& name, int id, Creator creator)
        {
            const auto already_defined = name_map.find(name) != std::end(name_map);
            assert(!already_defined);
            name_map[name] = std::move(creator);
            if(!already_defined)
            {
                const auto known_ids = ids();
                const auto it = std::find(known_ids.begin(), known_ids.end(), id);
                id = it == known_ids.end() ? id : get_next_id(known_ids);
                id_map[id] = name;
            }
            
        }

        [[nodiscard]] std::vector<std::string> names() const
        {
            std::vector<std::string> keys;
            for (const auto &[fst, snd] : name_map)
                keys.push_back(fst);
            return keys;
        }

        [[nodiscard]] std::vector<int> ids() const
        {
            std::vector<int> keys;
            for (const auto &[fst, snd] : id_map)
                keys.push_back(fst);
            return keys;
        }

        [[nodiscard]] std::unordered_map<int, std::string> map() const
        {
            return id_map;
        }

        [[nodiscard]]
        Type create(const std::string& name, Args ... params) const
        {
            const auto entry = name_map.find(name);
            assert(entry != std::end(name_map));
            return entry->second(std::forward<Args>(params)...);
        }
        
        [[nodiscard]]
        Type create(const int id, Args ... params) const
        {
            const auto entry = id_map.find(id);
            assert(entry != std::end(id_map));
            return create(entry->second, std::forward<Args>(params)...);
        }

    private:
        Factory() = default;
        Factory(const Factory &) = delete;
        std::unordered_map<std::string, Creator> name_map;
        std::unordered_map<int, std::string> id_map;
    };


   

    template <bool IsProblem>
    struct IdGetter
    {
    };

    template <>
    struct IdGetter<true>
    {
        template <typename T>
        static int get_id(const std::vector<int>&)
        {
            return T(1, 1).meta_data().problem_id;
        }
    };

    template <>
    struct IdGetter<false>
    {
        template <typename T>
        static int get_id(const std::vector<int>& ids)
        {
            return get_next_id(ids);
        }
    };


    template <typename Parent, typename ...Args>
    struct RegisterWithFactory
    {
        template <class T>
        static void include()
        {
            auto &factory = Factory<Parent, Args...>::instance();
            const auto is_problem_type = std::conjunction<std::is_same<int, Args>...>::value;
            const int id = IdGetter<is_problem_type>::template get_id<T>(factory.ids());

            factory.include(class_name<T>(), id, [](Args &&...params)
            {
                return std::make_unique<T>(std::forward<Args>(params)...);
            });
        }

        static Factory<Parent, Args...> &instance()
        {
            return Factory<Parent, Args...>::instance();
        }
    };


    template <class Type, class Factory>
    struct InvokeApplyOnConstruction
    {
        InvokeApplyOnConstruction()
        {
            Factory::template include<Type>();
        }
    };

    template <class Type, class Factory>
    struct RegistrationInvoker
    {
        static inline InvokeApplyOnConstruction<Type, Factory> registration_invoker = InvokeApplyOnConstruction<
            Type, Factory>();
    };


    template <class Type, class Factory>
    struct AutomaticTypeRegistration : RegistrationInvoker<Type, Factory>
    {
        InvokeApplyOnConstruction<Type, Factory> &invoker =
            RegistrationInvoker<Type, Factory>::registration_invoker;
    };
}
