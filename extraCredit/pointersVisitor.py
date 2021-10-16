# Generated from pointers.g4 by ANTLR 4.9.2
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by pointersParser.

class pointersVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by pointersParser#variableName.
    def visitVariableName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pointersParser#booleanExpression.
    def visitBooleanExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pointersParser#add.
    def visitAdd(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pointersParser#variableExpr.
    def visitVariableExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pointersParser#minus.
    def visitMinus(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pointersParser#paran.
    def visitParan(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pointersParser#divide.
    def visitDivide(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pointersParser#multiply.
    def visitMultiply(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pointersParser#literal.
    def visitLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pointersParser#skip.
    def visitSkip(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pointersParser#assign.
    def visitAssign(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pointersParser#if.
    def visitIf(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pointersParser#while.
    def visitWhile(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pointersParser#program.
    def visitProgram(self, ctx):
        return self.visitChildren(ctx)


