# Generated from SQLParser.g4 by ANTLR 4.7
from antlr4 import *



# This class defines a complete generic visitor for a parse tree produced by SQLParser.

class SQLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SQLParser#sql.
    def visitSql(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#statement.
    def visitStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#data_statement.
    def visitData_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#data_change_statement.
    def visitData_change_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#schema_statement.
    def visitSchema_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#index_statement.
    def visitIndex_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#create_table_statement.
    def visitCreate_table_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#table_elements.
    def visitTable_elements(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#field_element.
    def visitField_element(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#field_type.
    def visitField_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#param_clause.
    def visitParam_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#param.
    def visitParam(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#method_specifier.
    def visitMethod_specifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#table_space_specifier.
    def visitTable_space_specifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#table_space_name.
    def visitTable_space_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#table_partitioning_clauses.
    def visitTable_partitioning_clauses(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#range_partitions.
    def visitRange_partitions(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#range_value_clause_list.
    def visitRange_value_clause_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#range_value_clause.
    def visitRange_value_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#hash_partitions.
    def visitHash_partitions(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#individual_hash_partitions.
    def visitIndividual_hash_partitions(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#individual_hash_partition.
    def visitIndividual_hash_partition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#hash_partitions_by_quantity.
    def visitHash_partitions_by_quantity(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#list_partitions.
    def visitList_partitions(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#list_value_clause_list.
    def visitList_value_clause_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#list_value_partition.
    def visitList_value_partition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#column_partitions.
    def visitColumn_partitions(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#partition_name.
    def visitPartition_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#drop_table_statement.
    def visitDrop_table_statement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#identifier.
    def visitIdentifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#nonreserved_keywords.
    def visitNonreserved_keywords(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#unsigned_literal.
    def visitUnsigned_literal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#general_literal.
    def visitGeneral_literal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#datetime_literal.
    def visitDatetime_literal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#time_literal.
    def visitTime_literal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#timestamp_literal.
    def visitTimestamp_literal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#date_literal.
    def visitDate_literal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#boolean_literal.
    def visitBoolean_literal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#data_type.
    def visitData_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#predefined_type.
    def visitPredefined_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#network_type.
    def visitNetwork_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#character_string_type.
    def visitCharacter_string_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#type_length.
    def visitType_length(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#national_character_string_type.
    def visitNational_character_string_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#binary_large_object_string_type.
    def visitBinary_large_object_string_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#numeric_type.
    def visitNumeric_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#exact_numeric_type.
    def visitExact_numeric_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#approximate_numeric_type.
    def visitApproximate_numeric_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#precision_param.
    def visitPrecision_param(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#boolean_type.
    def visitBoolean_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#datetime_type.
    def visitDatetime_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#bit_type.
    def visitBit_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#binary_type.
    def visitBinary_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#value_expression_primary.
    def visitValue_expression_primary(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#parenthesized_value_expression.
    def visitParenthesized_value_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#nonparenthesized_value_expression_primary.
    def visitNonparenthesized_value_expression_primary(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#unsigned_value_specification.
    def visitUnsigned_value_specification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#unsigned_numeric_literal.
    def visitUnsigned_numeric_literal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#signed_numerical_literal.
    def visitSigned_numerical_literal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#set_function_specification.
    def visitSet_function_specification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#aggregate_function.
    def visitAggregate_function(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#general_set_function.
    def visitGeneral_set_function(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#set_function_type.
    def visitSet_function_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#filter_clause.
    def visitFilter_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#grouping_operation.
    def visitGrouping_operation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#case_expression.
    def visitCase_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#case_abbreviation.
    def visitCase_abbreviation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#case_specification.
    def visitCase_specification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#simple_case.
    def visitSimple_case(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#searched_case.
    def visitSearched_case(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#simple_when_clause.
    def visitSimple_when_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#searched_when_clause.
    def visitSearched_when_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#else_clause.
    def visitElse_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#result.
    def visitResult(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#cast_specification.
    def visitCast_specification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#cast_operand.
    def visitCast_operand(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#cast_target.
    def visitCast_target(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#value_expression.
    def visitValue_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#common_value_expression.
    def visitCommon_value_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#numeric_value_expression.
    def visitNumeric_value_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#term.
    def visitTerm(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#factor.
    def visitFactor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#array.
    def visitArray(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#numeric_primary.
    def visitNumeric_primary(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#sign.
    def visitSign(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#numeric_value_function.
    def visitNumeric_value_function(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#extract_expression.
    def visitExtract_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#extract_field.
    def visitExtract_field(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#time_zone_field.
    def visitTime_zone_field(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#extract_source.
    def visitExtract_source(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#string_value_expression.
    def visitString_value_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#character_value_expression.
    def visitCharacter_value_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#character_factor.
    def visitCharacter_factor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#character_primary.
    def visitCharacter_primary(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#string_value_function.
    def visitString_value_function(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#trim_function.
    def visitTrim_function(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#trim_operands.
    def visitTrim_operands(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#trim_specification.
    def visitTrim_specification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#boolean_value_expression.
    def visitBoolean_value_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#or_predicate.
    def visitOr_predicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#and_predicate.
    def visitAnd_predicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#boolean_factor.
    def visitBoolean_factor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#boolean_test.
    def visitBoolean_test(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#is_clause.
    def visitIs_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#truth_value.
    def visitTruth_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#boolean_primary.
    def visitBoolean_primary(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#boolean_predicand.
    def visitBoolean_predicand(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#parenthesized_boolean_value_expression.
    def visitParenthesized_boolean_value_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#row_value_expression.
    def visitRow_value_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#row_value_special_case.
    def visitRow_value_special_case(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#explicit_row_value_constructor.
    def visitExplicit_row_value_constructor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#row_value_predicand.
    def visitRow_value_predicand(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#row_value_constructor_predicand.
    def visitRow_value_constructor_predicand(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#table_expression.
    def visitTable_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#from_clause.
    def visitFrom_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#table_reference_list.
    def visitTable_reference_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#table_reference.
    def visitTable_reference(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#joined_table.
    def visitJoined_table(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#joined_table_primary.
    def visitJoined_table_primary(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#cross_join.
    def visitCross_join(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#qualified_join.
    def visitQualified_join(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#natural_join.
    def visitNatural_join(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#union_join.
    def visitUnion_join(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#join_type.
    def visitJoin_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#outer_join_type.
    def visitOuter_join_type(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#outer_join_type_part2.
    def visitOuter_join_type_part2(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#join_specification.
    def visitJoin_specification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#join_condition.
    def visitJoin_condition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#named_columns_join.
    def visitNamed_columns_join(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#table_primary.
    def visitTable_primary(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#column_name_list.
    def visitColumn_name_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#derived_table.
    def visitDerived_table(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#where_clause.
    def visitWhere_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#search_condition.
    def visitSearch_condition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#groupby_clause.
    def visitGroupby_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#grouping_element_list.
    def visitGrouping_element_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#grouping_element.
    def visitGrouping_element(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#ordinary_grouping_set.
    def visitOrdinary_grouping_set(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#ordinary_grouping_set_list.
    def visitOrdinary_grouping_set_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#rollup_list.
    def visitRollup_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#cube_list.
    def visitCube_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#empty_grouping_set.
    def visitEmpty_grouping_set(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#having_clause.
    def visitHaving_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#row_value_predicand_list.
    def visitRow_value_predicand_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#query_expression.
    def visitQuery_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#query_expression_body.
    def visitQuery_expression_body(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#non_join_query_expression.
    def visitNon_join_query_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#query_term.
    def visitQuery_term(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#non_join_query_term.
    def visitNon_join_query_term(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#query_primary.
    def visitQuery_primary(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#non_join_query_primary.
    def visitNon_join_query_primary(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#simple_table.
    def visitSimple_table(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#explicit_table.
    def visitExplicit_table(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#table_or_query_name.
    def visitTable_or_query_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#table_name.
    def visitTable_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#query_specification.
    def visitQuery_specification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#select_list.
    def visitSelect_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#select_sublist.
    def visitSelect_sublist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#derived_column.
    def visitDerived_column(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#qualified_asterisk.
    def visitQualified_asterisk(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#set_qualifier.
    def visitSet_qualifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#column_reference.
    def visitColumn_reference(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#as_clause.
    def visitAs_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#column_reference_list.
    def visitColumn_reference_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#scalar_subquery.
    def visitScalar_subquery(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#row_subquery.
    def visitRow_subquery(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#table_subquery.
    def visitTable_subquery(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#subquery.
    def visitSubquery(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#predicate.
    def visitPredicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#comparison_predicate.
    def visitComparison_predicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#comp_op.
    def visitComp_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#between_predicate.
    def visitBetween_predicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#between_predicate_part_2.
    def visitBetween_predicate_part_2(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#in_predicate.
    def visitIn_predicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#in_predicate_value.
    def visitIn_predicate_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#in_value_list.
    def visitIn_value_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#pattern_matching_predicate.
    def visitPattern_matching_predicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#pattern_matcher.
    def visitPattern_matcher(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#negativable_matcher.
    def visitNegativable_matcher(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#regex_matcher.
    def visitRegex_matcher(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#null_predicate.
    def visitNull_predicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#quantified_comparison_predicate.
    def visitQuantified_comparison_predicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#quantifier.
    def visitQuantifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#all.
    def visitAll(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#some.
    def visitSome(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#exists_predicate.
    def visitExists_predicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#unique_predicate.
    def visitUnique_predicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#primary_datetime_field.
    def visitPrimary_datetime_field(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#non_second_primary_datetime_field.
    def visitNon_second_primary_datetime_field(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#extended_datetime_field.
    def visitExtended_datetime_field(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#routine_invocation.
    def visitRoutine_invocation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#function_names_for_reserved_words.
    def visitFunction_names_for_reserved_words(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#function_name.
    def visitFunction_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#sql_argument_list.
    def visitSql_argument_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#orderby_clause.
    def visitOrderby_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#sort_specifier_list.
    def visitSort_specifier_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#sort_specifier.
    def visitSort_specifier(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#order_specification.
    def visitOrder_specification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#limit_clause.
    def visitLimit_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#null_ordering.
    def visitNull_ordering(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#insert_statement.
    def visitInsert_statement(self, ctx):
        return self.visitChildren(ctx)