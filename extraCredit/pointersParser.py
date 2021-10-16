# Generated from pointers.g4 by ANTLR 4.9.2
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\32h\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\30\n\3\3\4\3")
        buf.write(u"\4\3\4\3\4\3\4\3\4\3\4\5\4!\n\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write(u"\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4/\n\4\f\4\16\4\62\13\4")
        buf.write(u"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\6\5?\n\5")
        buf.write(u"\r\5\16\5@\3\5\3\5\3\5\3\5\3\5\3\5\6\5I\n\5\r\5\16\5")
        buf.write(u"J\3\5\3\5\5\5O\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\6")
        buf.write(u"\5Y\n\5\r\5\16\5Z\3\5\3\5\5\5_\n\5\3\6\3\6\3\6\6\6d\n")
        buf.write(u"\6\r\6\16\6e\3\6\2\3\6\7\2\4\6\b\n\2\2\2r\2\f\3\2\2\2")
        buf.write(u"\4\27\3\2\2\2\6 \3\2\2\2\b^\3\2\2\2\nc\3\2\2\2\f\r\7")
        buf.write(u"\22\2\2\r\3\3\2\2\2\16\30\7\23\2\2\17\20\5\6\4\2\20\21")
        buf.write(u"\7\30\2\2\21\22\5\6\4\2\22\30\3\2\2\2\23\24\5\6\4\2\24")
        buf.write(u"\25\7\31\2\2\25\26\5\6\4\2\26\30\3\2\2\2\27\16\3\2\2")
        buf.write(u"\2\27\17\3\2\2\2\27\23\3\2\2\2\30\5\3\2\2\2\31\32\b\4")
        buf.write(u"\1\2\32!\7\23\2\2\33!\5\2\2\2\34\35\7\3\2\2\35\36\5\6")
        buf.write(u"\4\2\36\37\7\4\2\2\37!\3\2\2\2 \31\3\2\2\2 \33\3\2\2")
        buf.write(u"\2 \34\3\2\2\2!\60\3\2\2\2\"#\f\6\2\2#$\7\26\2\2$/\5")
        buf.write(u"\6\4\7%&\f\5\2\2&\'\7\27\2\2\'/\5\6\4\6()\f\4\2\2)*\7")
        buf.write(u"\24\2\2*/\5\6\4\5+,\f\3\2\2,-\7\25\2\2-/\5\6\4\4.\"\3")
        buf.write(u"\2\2\2.%\3\2\2\2.(\3\2\2\2.+\3\2\2\2/\62\3\2\2\2\60.")
        buf.write(u"\3\2\2\2\60\61\3\2\2\2\61\7\3\2\2\2\62\60\3\2\2\2\63")
        buf.write(u"_\7\t\2\2\64\65\5\2\2\2\65\66\7\5\2\2\66\67\5\6\4\2\67")
        buf.write(u"_\3\2\2\289\7\13\2\29:\5\6\4\2:>\7\6\2\2;<\5\b\5\2<=")
        buf.write(u"\7\7\2\2=?\3\2\2\2>;\3\2\2\2?@\3\2\2\2@>\3\2\2\2@A\3")
        buf.write(u"\2\2\2AB\3\2\2\2BN\7\b\2\2CD\7\r\2\2DH\7\6\2\2EF\5\b")
        buf.write(u"\5\2FG\7\7\2\2GI\3\2\2\2HE\3\2\2\2IJ\3\2\2\2JH\3\2\2")
        buf.write(u"\2JK\3\2\2\2KL\3\2\2\2LM\7\b\2\2MO\3\2\2\2NC\3\2\2\2")
        buf.write(u"NO\3\2\2\2O_\3\2\2\2PQ\7\17\2\2QR\7\3\2\2RS\5\6\4\2S")
        buf.write(u"T\7\4\2\2TX\7\6\2\2UV\5\b\5\2VW\7\7\2\2WY\3\2\2\2XU\3")
        buf.write(u"\2\2\2YZ\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[\\\3\2\2\2\\]\7")
        buf.write(u"\b\2\2]_\3\2\2\2^\63\3\2\2\2^\64\3\2\2\2^8\3\2\2\2^P")
        buf.write(u"\3\2\2\2_\t\3\2\2\2`a\5\b\5\2ab\7\7\2\2bd\3\2\2\2c`\3")
        buf.write(u"\2\2\2de\3\2\2\2ec\3\2\2\2ef\3\2\2\2f\13\3\2\2\2\f\27")
        buf.write(u" .\60@JNZ^e")
        return buf.getvalue()


class pointersParser ( Parser ):

    grammarFileName = "pointers.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'('", u"')'", u"'='", u"'{'", u"';'", 
                     u"'}'", u"'skip'", u"'malloc'", u"'if'", u"'then'", 
                     u"'else'", u"'done'", u"'while'", u"'do'", u"'od'", 
                     u"<INVALID>", u"<INVALID>", u"'+'", u"'-'", u"'*'", 
                     u"'/'", u"'=='", u"'<'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"SKIPSTATEMENT", 
                      u"MALLOC", u"IF", u"THEN", u"ELSE", u"DONE", u"WHILE", 
                      u"DO", u"OD", u"VAR", u"INT", u"PLUS", u"MINUS", u"MULTIPLY", 
                      u"DIVISION", u"EQUALS", u"LEQ", u"WHITESPACE" ]

    RULE_variable = 0
    RULE_booleanExpression = 1
    RULE_expression = 2
    RULE_statement = 3
    RULE_program = 4

    ruleNames =  [ u"variable", u"booleanExpression", u"expression", u"statement", 
                   u"program" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    SKIPSTATEMENT=7
    MALLOC=8
    IF=9
    THEN=10
    ELSE=11
    DONE=12
    WHILE=13
    DO=14
    OD=15
    VAR=16
    INT=17
    PLUS=18
    MINUS=19
    MULTIPLY=20
    DIVISION=21
    EQUALS=22
    LEQ=23
    WHITESPACE=24

    def __init__(self, input, output=sys.stdout):
        super(pointersParser, self).__init__(input, output=output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(pointersParser.VariableContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pointersParser.RULE_variable

     
        def copyFrom(self, ctx):
            super(pointersParser.VariableContext, self).copyFrom(ctx)



    class VariableNameContext(VariableContext):

        def __init__(self, parser, ctx): # actually a pointersParser.VariableContext)
            super(pointersParser.VariableNameContext, self).__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(pointersParser.VAR, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterVariableName"):
                listener.enterVariableName(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVariableName"):
                listener.exitVariableName(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitVariableName"):
                return visitor.visitVariableName(self)
            else:
                return visitor.visitChildren(self)



    def variable(self):

        localctx = pointersParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_variable)
        try:
            localctx = pointersParser.VariableNameContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(pointersParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(pointersParser.BooleanExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(pointersParser.INT, 0)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(pointersParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pointersParser.ExpressionContext,i)


        def EQUALS(self):
            return self.getToken(pointersParser.EQUALS, 0)

        def LEQ(self):
            return self.getToken(pointersParser.LEQ, 0)

        def getRuleIndex(self):
            return pointersParser.RULE_booleanExpression

        def enterRule(self, listener):
            if hasattr(listener, "enterBooleanExpression"):
                listener.enterBooleanExpression(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBooleanExpression"):
                listener.exitBooleanExpression(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitBooleanExpression"):
                return visitor.visitBooleanExpression(self)
            else:
                return visitor.visitChildren(self)




    def booleanExpression(self):

        localctx = pointersParser.BooleanExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_booleanExpression)
        try:
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.match(pointersParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.expression(0)
                self.state = 14
                self.match(pointersParser.EQUALS)
                self.state = 15
                self.expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 17
                self.expression(0)
                self.state = 18
                self.match(pointersParser.LEQ)
                self.state = 19
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(pointersParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pointersParser.RULE_expression

     
        def copyFrom(self, ctx):
            super(pointersParser.ExpressionContext, self).copyFrom(ctx)


    class AddContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a pointersParser.ExpressionContext)
            super(pointersParser.AddContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(pointersParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pointersParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(pointersParser.PLUS, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAdd"):
                listener.enterAdd(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAdd"):
                listener.exitAdd(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAdd"):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class VariableExprContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a pointersParser.ExpressionContext)
            super(pointersParser.VariableExprContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(pointersParser.VariableContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterVariableExpr"):
                listener.enterVariableExpr(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVariableExpr"):
                listener.exitVariableExpr(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitVariableExpr"):
                return visitor.visitVariableExpr(self)
            else:
                return visitor.visitChildren(self)


    class MinusContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a pointersParser.ExpressionContext)
            super(pointersParser.MinusContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(pointersParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pointersParser.ExpressionContext,i)

        def MINUS(self):
            return self.getToken(pointersParser.MINUS, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterMinus"):
                listener.enterMinus(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMinus"):
                listener.exitMinus(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitMinus"):
                return visitor.visitMinus(self)
            else:
                return visitor.visitChildren(self)


    class ParanContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a pointersParser.ExpressionContext)
            super(pointersParser.ParanContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(pointersParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterParan"):
                listener.enterParan(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParan"):
                listener.exitParan(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitParan"):
                return visitor.visitParan(self)
            else:
                return visitor.visitChildren(self)


    class DivideContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a pointersParser.ExpressionContext)
            super(pointersParser.DivideContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(pointersParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pointersParser.ExpressionContext,i)

        def DIVISION(self):
            return self.getToken(pointersParser.DIVISION, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterDivide"):
                listener.enterDivide(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDivide"):
                listener.exitDivide(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitDivide"):
                return visitor.visitDivide(self)
            else:
                return visitor.visitChildren(self)


    class MultiplyContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a pointersParser.ExpressionContext)
            super(pointersParser.MultiplyContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(pointersParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(pointersParser.ExpressionContext,i)

        def MULTIPLY(self):
            return self.getToken(pointersParser.MULTIPLY, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterMultiply"):
                listener.enterMultiply(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMultiply"):
                listener.exitMultiply(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitMultiply"):
                return visitor.visitMultiply(self)
            else:
                return visitor.visitChildren(self)


    class LiteralContext(ExpressionContext):

        def __init__(self, parser, ctx): # actually a pointersParser.ExpressionContext)
            super(pointersParser.LiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(pointersParser.INT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteral"):
                listener.enterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteral"):
                listener.exitLiteral(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitLiteral"):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = pointersParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pointersParser.INT]:
                localctx = pointersParser.LiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 24
                self.match(pointersParser.INT)
                pass
            elif token in [pointersParser.VAR]:
                localctx = pointersParser.VariableExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.variable()
                pass
            elif token in [pointersParser.T__0]:
                localctx = pointersParser.ParanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(pointersParser.T__0)
                self.state = 27
                self.expression(0)
                self.state = 28
                self.match(pointersParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 44
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = pointersParser.MultiplyContext(self, pointersParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 32
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 33
                        self.match(pointersParser.MULTIPLY)
                        self.state = 34
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = pointersParser.DivideContext(self, pointersParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 35
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 36
                        self.match(pointersParser.DIVISION)
                        self.state = 37
                        self.expression(4)
                        pass

                    elif la_ == 3:
                        localctx = pointersParser.AddContext(self, pointersParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 38
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 39
                        self.match(pointersParser.PLUS)
                        self.state = 40
                        self.expression(3)
                        pass

                    elif la_ == 4:
                        localctx = pointersParser.MinusContext(self, pointersParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 41
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 42
                        self.match(pointersParser.MINUS)
                        self.state = 43
                        self.expression(2)
                        pass

             
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(pointersParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pointersParser.RULE_statement

     
        def copyFrom(self, ctx):
            super(pointersParser.StatementContext, self).copyFrom(ctx)



    class SkipContext(StatementContext):

        def __init__(self, parser, ctx): # actually a pointersParser.StatementContext)
            super(pointersParser.SkipContext, self).__init__(parser)
            self.copyFrom(ctx)

        def SKIPSTATEMENT(self):
            return self.getToken(pointersParser.SKIPSTATEMENT, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterSkip"):
                listener.enterSkip(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSkip"):
                listener.exitSkip(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitSkip"):
                return visitor.visitSkip(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(StatementContext):

        def __init__(self, parser, ctx): # actually a pointersParser.StatementContext)
            super(pointersParser.WhileContext, self).__init__(parser)
            self.cond = None # ExpressionContext
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(pointersParser.WHILE, 0)
        def expression(self):
            return self.getTypedRuleContext(pointersParser.ExpressionContext,0)

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(pointersParser.StatementContext)
            else:
                return self.getTypedRuleContext(pointersParser.StatementContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterWhile"):
                listener.enterWhile(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitWhile"):
                listener.exitWhile(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitWhile"):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(StatementContext):

        def __init__(self, parser, ctx): # actually a pointersParser.StatementContext)
            super(pointersParser.IfContext, self).__init__(parser)
            self.cond = None # ExpressionContext
            self._statement = None # StatementContext
            self.ifs = list() # of StatementContexts
            self.elses = list() # of StatementContexts
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(pointersParser.IF, 0)
        def expression(self):
            return self.getTypedRuleContext(pointersParser.ExpressionContext,0)

        def ELSE(self):
            return self.getToken(pointersParser.ELSE, 0)
        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(pointersParser.StatementContext)
            else:
                return self.getTypedRuleContext(pointersParser.StatementContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterIf"):
                listener.enterIf(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIf"):
                listener.exitIf(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitIf"):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatementContext):

        def __init__(self, parser, ctx): # actually a pointersParser.StatementContext)
            super(pointersParser.AssignContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(pointersParser.VariableContext,0)

        def expression(self):
            return self.getTypedRuleContext(pointersParser.ExpressionContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterAssign"):
                listener.enterAssign(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAssign"):
                listener.exitAssign(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAssign"):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = pointersParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pointersParser.SKIPSTATEMENT]:
                localctx = pointersParser.SkipContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(pointersParser.SKIPSTATEMENT)
                pass
            elif token in [pointersParser.VAR]:
                localctx = pointersParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.variable()
                self.state = 51
                self.match(pointersParser.T__2)
                self.state = 52
                self.expression(0)
                pass
            elif token in [pointersParser.IF]:
                localctx = pointersParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.match(pointersParser.IF)
                self.state = 55
                localctx.cond = self.expression(0)
                self.state = 56
                self.match(pointersParser.T__3)
                self.state = 60 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 57
                    localctx._statement = self.statement()
                    localctx.ifs.append(localctx._statement)
                    self.state = 58
                    self.match(pointersParser.T__4)
                    self.state = 62 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pointersParser.SKIPSTATEMENT) | (1 << pointersParser.IF) | (1 << pointersParser.WHILE) | (1 << pointersParser.VAR))) != 0)):
                        break

                self.state = 64
                self.match(pointersParser.T__5)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==pointersParser.ELSE:
                    self.state = 65
                    self.match(pointersParser.ELSE)
                    self.state = 66
                    self.match(pointersParser.T__3)
                    self.state = 70 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 67
                        localctx._statement = self.statement()
                        localctx.elses.append(localctx._statement)
                        self.state = 68
                        self.match(pointersParser.T__4)
                        self.state = 72 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pointersParser.SKIPSTATEMENT) | (1 << pointersParser.IF) | (1 << pointersParser.WHILE) | (1 << pointersParser.VAR))) != 0)):
                            break

                    self.state = 74
                    self.match(pointersParser.T__5)


                pass
            elif token in [pointersParser.WHILE]:
                localctx = pointersParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.match(pointersParser.WHILE)
                self.state = 79
                self.match(pointersParser.T__0)
                self.state = 80
                localctx.cond = self.expression(0)
                self.state = 81
                self.match(pointersParser.T__1)
                self.state = 82
                self.match(pointersParser.T__3)
                self.state = 86 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 83
                    self.statement()
                    self.state = 84
                    self.match(pointersParser.T__4)
                    self.state = 88 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pointersParser.SKIPSTATEMENT) | (1 << pointersParser.IF) | (1 << pointersParser.WHILE) | (1 << pointersParser.VAR))) != 0)):
                        break

                self.state = 90
                self.match(pointersParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(pointersParser.ProgramContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(pointersParser.StatementContext)
            else:
                return self.getTypedRuleContext(pointersParser.StatementContext,i)


        def getRuleIndex(self):
            return pointersParser.RULE_program

        def enterRule(self, listener):
            if hasattr(listener, "enterProgram"):
                listener.enterProgram(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitProgram"):
                listener.exitProgram(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitProgram"):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = pointersParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 94
                self.statement()
                self.state = 95
                self.match(pointersParser.T__4)
                self.state = 99 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pointersParser.SKIPSTATEMENT) | (1 << pointersParser.IF) | (1 << pointersParser.WHILE) | (1 << pointersParser.VAR))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




