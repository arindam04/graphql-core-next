"""graphql.validation.rules package"""

from typing import Type

from ...error import GraphQLError
from ...language.visitor import Visitor
from ..validation_context import (
    ASTValidationContext,
    SDLValidationContext,
    ValidationContext,
)

__all__ = ["ASTValidationRule", "SDLValidationRule", "ValidationRule", "RuleType"]


class ASTValidationRule(Visitor):
    """Visitor for validation of an AST."""

    context: ASTValidationContext

    def __init__(self, context: ASTValidationContext):
        self.context = context

    def report_error(self, error: GraphQLError):
        self.context.report_error(error)


class SDLValidationRule(ASTValidationRule):
    """Visitor for validation of an SDL AST."""

    context: ValidationContext

    def __init__(self, context: SDLValidationContext):
        super().__init__(context)


class ValidationRule(ASTValidationRule):
    """Visitor for validation using a GraphQL schema."""

    context: ValidationContext

    def __init__(self, context: ValidationContext):
        super().__init__(context)


RuleType = Type[ASTValidationRule]
