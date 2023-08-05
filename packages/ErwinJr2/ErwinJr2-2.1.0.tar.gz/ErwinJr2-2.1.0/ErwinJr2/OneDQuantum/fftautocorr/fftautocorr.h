/**
 * @file fftautocorr.h
 * @author CareF <CareF.LM@gmail.com>
 * @brief Header definition for fftautocorr
 * @version 0.1
 * @date 2020-07-04
 * 
 * This file is part of fftautocorr
 * 
 * @copyright Copyright (c) 2020 
 *            Licensed under a 3-clause BSD style license - see LICENSE.md
 */

#ifndef FFTAUTOCORR_H
#define FFTAUTOCORR_H

#include <stdlib.h>

/**
 * @brief The internal struct for FFT plan. 
 * 
 * Should not be directly used by the user.
 */
struct autocorr_plan_i;

/**
 * @brief The FFT plan. 
 * 
 * Created by make_autocorr_plan()
 */
typedef struct autocorr_plan_i * autocorr_plan;

/**
 * @brief Create an autocorr_plan for later calculation.
 * 
 * destroy_autocorr_plan() must be called on the function to avoid memory leak.
 * 
 * @param[in] length The length for input data array.
 * @return autocorr_plan The plan to be used for calculation.
 */
autocorr_plan make_autocorr_plan(size_t length);

/**
 * @brief Destroy the plan to release memory.
 * 
 * @param[in] plan the plan to be destroyed.
 */
void destroy_autocorr_plan(autocorr_plan plan);

/**
 * @brief Get the length of the memory needed for a plan.
 * 
 * The memory needed is at least 2 times the size of the input data.
 * 
 * @param[in] plan The plan to get the memory needed for.
 * @return The size of the memory needed.
 */
size_t mem_len(autocorr_plan plan);

/**
 * @brief The logical length (length of input and output data) for the 
 *        calculation.
 * 
 * @param[in] plan The plan to get the logical length for.
 * @return The logical length.
 */
size_t data_len(autocorr_plan plan);

/**
 * @brief One stop solution to calculate the autocorrelation for \p data with 
 *        size \p length.
 * 
 * @param[in,out] data The input data and the output autocorrelation.
 * @param[in] length The length of the input data.
 * @return 0 for success, -1 for fail.
 */
int autocorr(double data[], size_t length);

/**
 * @brief Calcualte the autocorrelation using the given \p plan.
 * 
 * @param[in] plan The plan for the calculation
 * @param[in,out] data Input and output data, with length defined i
 * @return 0 for success, -1 for fail.
 */
int autocorr_p(autocorr_plan plan, double data[]);

/**
 * @brief Calcualate autocorrelation using \p plan for FFT and \mempool for
 *        the mem used in the calculation.
 * 
 * @param[in] plan FFT plan generated by make_autocorr_plan()
 * @param[in,out] data The data to be calculated from, and also the output for
 *                     the autocorrelation result.
 * @param[in] mempool The address for memory needed for the autocorrelationm. needs
 *                to be at least ::mem_len(plan)*sizeof(double) long.
 * @return 0 for success, -1 for fail.
 */
int autocorr_mem(autocorr_plan plan, double data[], double *mempool);

#endif /* ifndef FFTAUTOCORR_H */
