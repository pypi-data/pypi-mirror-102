#pragma once
#include "ioh/problem/utils.hpp"
#include "pbo_problem.hpp"

namespace ioh
{
    namespace problem
    {
        namespace pbo
        {
            class LeadingOnesNeutrality final: public PBOProblem<LeadingOnesNeutrality>
            {
            protected:
                std::vector<double> evaluate(const std::vector<int> &x) override
                {
                    auto new_variables = utils::neutrality(x, 3);
                    size_t result = 0;
                    for (size_t i = 0; i < new_variables.size(); ++i)
                        if (new_variables[i] == 1)
                            result = i + 1;
                        else
                            break;
                    return {static_cast<double>(result)};
                }

            public:
                /**
                 * \brief Construct a new LeadingOnes_Neutrality object. Definition refers to
                 *https://doi.org/10.1016/j.asoc.2019.106027
                 *
                 * \param instance The instance number of a problem, which controls the transformation
                 * performed on the original problem.
                 * \param n_variables The dimensionality of the problem to created, 4 by default.
                 **/
                LeadingOnesNeutrality(const int instance, const int n_variables) :
                    PBOProblem(13, instance, n_variables, "LeadingOnesNeutrality")
                {
                    objective_.x = std::vector<int>(n_variables,1);
                    objective_.y = evaluate(objective_.x);
                }
            };
        } // namespace pbo
    } // namespace problem
} // namespace ioh
