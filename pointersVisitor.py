# Generated from pointers.g4 by ANTLR 4.9.2
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by pointersParser.

class pointersVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by pointersParser#variableName.
    def visitVariableName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pointersParser#nullvar.
    def visitNullvar(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pointersParser#skip.
    def visitSkip(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pointersParser#alloc.
    def visitAlloc(self, ctx):
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


