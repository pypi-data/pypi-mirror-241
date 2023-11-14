//===----------------------------------------------------------------------===//
//                         DuckDB
//
// duckdb/core_functions/aggregate/distributive_functions.hpp
//
//
//===----------------------------------------------------------------------===//
// This file is automatically generated by scripts/generate_functions.py
// Do not edit this file manually, your changes will be overwritten
//===----------------------------------------------------------------------===//

#pragma once

#include "duckdb/function/function_set.hpp"

namespace duckdb {

struct ApproxCountDistinctFun {
	static constexpr const char *Name = "approx_count_distinct";
	static constexpr const char *Parameters = "x";
	static constexpr const char *Description = "Computes the approximate count of distinct elements using HyperLogLog.";
	static constexpr const char *Example = "approx_count_distinct(A)";

	static AggregateFunctionSet GetFunctions();
};

struct ArgMinFun {
	static constexpr const char *Name = "arg_min";
	static constexpr const char *Parameters = "arg,val";
	static constexpr const char *Description = "Finds the row with the minimum val. Calculates the arg expression at that row.";
	static constexpr const char *Example = "arg_min(A,B)";

	static AggregateFunctionSet GetFunctions();
};

struct ArgminFun {
	using ALIAS = ArgMinFun;

	static constexpr const char *Name = "argmin";
};

struct MinByFun {
	using ALIAS = ArgMinFun;

	static constexpr const char *Name = "min_by";
};

struct ArgMaxFun {
	static constexpr const char *Name = "arg_max";
	static constexpr const char *Parameters = "arg,val";
	static constexpr const char *Description = "Finds the row with the maximum val. Calculates the arg expression at that row.";
	static constexpr const char *Example = "arg_max(A,B)";

	static AggregateFunctionSet GetFunctions();
};

struct ArgmaxFun {
	using ALIAS = ArgMaxFun;

	static constexpr const char *Name = "argmax";
};

struct MaxByFun {
	using ALIAS = ArgMaxFun;

	static constexpr const char *Name = "max_by";
};

struct BitAndFun {
	static constexpr const char *Name = "bit_and";
	static constexpr const char *Parameters = "arg";
	static constexpr const char *Description = "Returns the bitwise AND of all bits in a given expression.";
	static constexpr const char *Example = "bit_and(A)";

	static AggregateFunctionSet GetFunctions();
};

struct BitOrFun {
	static constexpr const char *Name = "bit_or";
	static constexpr const char *Parameters = "arg";
	static constexpr const char *Description = "Returns the bitwise OR of all bits in a given expression.";
	static constexpr const char *Example = "bit_or(A)";

	static AggregateFunctionSet GetFunctions();
};

struct BitXorFun {
	static constexpr const char *Name = "bit_xor";
	static constexpr const char *Parameters = "arg";
	static constexpr const char *Description = "Returns the bitwise XOR of all bits in a given expression.";
	static constexpr const char *Example = "bit_xor(A)";

	static AggregateFunctionSet GetFunctions();
};

struct BitstringAggFun {
	static constexpr const char *Name = "bitstring_agg";
	static constexpr const char *Parameters = "arg";
	static constexpr const char *Description = "Returns a bitstring with bits set for each distinct value.";
	static constexpr const char *Example = "bitstring_agg(A)";

	static AggregateFunctionSet GetFunctions();
};

struct BoolAndFun {
	static constexpr const char *Name = "bool_and";
	static constexpr const char *Parameters = "arg";
	static constexpr const char *Description = "Returns TRUE if every input value is TRUE, otherwise FALSE.";
	static constexpr const char *Example = "bool_and(A)";

	static AggregateFunction GetFunction();
};

struct BoolOrFun {
	static constexpr const char *Name = "bool_or";
	static constexpr const char *Parameters = "arg";
	static constexpr const char *Description = "Returns TRUE if any input value is TRUE, otherwise FALSE.";
	static constexpr const char *Example = "bool_or(A)";

	static AggregateFunction GetFunction();
};

struct EntropyFun {
	static constexpr const char *Name = "entropy";
	static constexpr const char *Parameters = "x";
	static constexpr const char *Description = "Returns the log-2 entropy of count input-values.";
	static constexpr const char *Example = "";

	static AggregateFunctionSet GetFunctions();
};

struct KahanSumFun {
	static constexpr const char *Name = "kahan_sum";
	static constexpr const char *Parameters = "arg";
	static constexpr const char *Description = "Calculates the sum using a more accurate floating point summation (Kahan Sum).";
	static constexpr const char *Example = "kahan_sum(A)";

	static AggregateFunction GetFunction();
};

struct FsumFun {
	using ALIAS = KahanSumFun;

	static constexpr const char *Name = "fsum";
};

struct SumkahanFun {
	using ALIAS = KahanSumFun;

	static constexpr const char *Name = "sumkahan";
};

struct KurtosisFun {
	static constexpr const char *Name = "kurtosis";
	static constexpr const char *Parameters = "x";
	static constexpr const char *Description = "Returns the excess kurtosis (Fisher’s definition) of all input values, with a bias correction according to the sample size";
	static constexpr const char *Example = "";

	static AggregateFunction GetFunction();
};

struct MinFun {
	static constexpr const char *Name = "min";
	static constexpr const char *Parameters = "arg";
	static constexpr const char *Description = "Returns the minimum value present in arg.";
	static constexpr const char *Example = "min(A)";

	static AggregateFunctionSet GetFunctions();
};

struct MaxFun {
	static constexpr const char *Name = "max";
	static constexpr const char *Parameters = "arg";
	static constexpr const char *Description = "Returns the maximum value present in arg.";
	static constexpr const char *Example = "max(A)";

	static AggregateFunctionSet GetFunctions();
};

struct ProductFun {
	static constexpr const char *Name = "product";
	static constexpr const char *Parameters = "arg";
	static constexpr const char *Description = "Calculates the product of all tuples in arg.";
	static constexpr const char *Example = "product(A)";

	static AggregateFunction GetFunction();
};

struct SkewnessFun {
	static constexpr const char *Name = "skewness";
	static constexpr const char *Parameters = "x";
	static constexpr const char *Description = "Returns the skewness of all input values.";
	static constexpr const char *Example = "skewness(A)";

	static AggregateFunction GetFunction();
};

struct StringAggFun {
	static constexpr const char *Name = "string_agg";
	static constexpr const char *Parameters = "str,arg";
	static constexpr const char *Description = "Concatenates the column string values with an optional separator.";
	static constexpr const char *Example = "string_agg(A, '-')";

	static AggregateFunctionSet GetFunctions();
};

struct GroupConcatFun {
	using ALIAS = StringAggFun;

	static constexpr const char *Name = "group_concat";
};

struct ListaggFun {
	using ALIAS = StringAggFun;

	static constexpr const char *Name = "listagg";
};

struct SumFun {
	static constexpr const char *Name = "sum";
	static constexpr const char *Parameters = "arg";
	static constexpr const char *Description = "Calculates the sum value for all tuples in arg.";
	static constexpr const char *Example = "sum(A)";

	static AggregateFunctionSet GetFunctions();
};

struct SumNoOverflowFun {
	static constexpr const char *Name = "sum_no_overflow";
	static constexpr const char *Parameters = "arg";
	static constexpr const char *Description = "Calculates the sum value for all tuples in arg without overflow checks.";
	static constexpr const char *Example = "sum_no_overflow(A)";

	static AggregateFunctionSet GetFunctions();
};

} // namespace duckdb
