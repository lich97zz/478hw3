# Generated from pointers.g4 by ANTLR 4.9.2
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\33H\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\5\2\13\n\2\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\6\3\37\n\3\r\3\16\3 \3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\6\3)\n\3\r\3\16\3*\3\3\3\3\5\3/\n\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\6\39\n\3\r\3\16\3:\3\3\3\3\5\3")
        buf.write(u"?\n\3\3\4\3\4\3\4\6\4D\n\4\r\4\16\4E\3\4\2\2\5\2\4\6")
        buf.write(u"\2\2\2N\2\n\3\2\2\2\4>\3\2\2\2\6C\3\2\2\2\b\13\7\23\2")
        buf.write(u"\2\t\13\7\22\2\2\n\b\3\2\2\2\n\t\3\2\2\2\13\3\3\2\2\2")
        buf.write(u"\f?\7\t\2\2\r\16\5\2\2\2\16\17\7\3\2\2\17\20\7\n\2\2")
        buf.write(u"\20\21\7\23\2\2\21?\3\2\2\2\22\23\5\2\2\2\23\24\7\3\2")
        buf.write(u"\2\24\25\5\2\2\2\25?\3\2\2\2\26\27\7\13\2\2\27\30\7\4")
        buf.write(u"\2\2\30\31\5\2\2\2\31\32\7\5\2\2\32\36\7\6\2\2\33\34")
        buf.write(u"\5\4\3\2\34\35\7\7\2\2\35\37\3\2\2\2\36\33\3\2\2\2\37")
        buf.write(u" \3\2\2\2 \36\3\2\2\2 !\3\2\2\2!\"\3\2\2\2\".\7\b\2\2")
        buf.write(u"#$\7\r\2\2$(\7\6\2\2%&\5\4\3\2&\'\7\7\2\2\')\3\2\2\2")
        buf.write(u"(%\3\2\2\2)*\3\2\2\2*(\3\2\2\2*+\3\2\2\2+,\3\2\2\2,-")
        buf.write(u"\7\b\2\2-/\3\2\2\2.#\3\2\2\2./\3\2\2\2/?\3\2\2\2\60\61")
        buf.write(u"\7\17\2\2\61\62\7\4\2\2\62\63\5\2\2\2\63\64\7\5\2\2\64")
        buf.write(u"8\7\6\2\2\65\66\5\4\3\2\66\67\7\7\2\2\679\3\2\2\28\65")
        buf.write(u"\3\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;<\3\2\2\2<=\7")
        buf.write(u"\b\2\2=?\3\2\2\2>\f\3\2\2\2>\r\3\2\2\2>\22\3\2\2\2>\26")
        buf.write(u"\3\2\2\2>\60\3\2\2\2?\5\3\2\2\2@A\5\4\3\2AB\7\7\2\2B")
        buf.write(u"D\3\2\2\2C@\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2F\7")
        buf.write(u"\3\2\2\2\t\n *.:>E")
        return buf.getvalue()


class pointersParser ( Parser ):

    grammarFileName = "pointers.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"':='", u"'('", u"')'", u"'{'", u"';'", 
                     u"'}'", u"'skip'", u"'newObject'", u"'if'", u"'then'", 
                     u"'else'", u"'done'", u"'while'", u"'do'", u"'od'", 
                     u"'null'", u"<INVALID>", u"<INVALID>", u"'+'", u"'-'", 
                     u"'*'", u"'/'", u"'=='", u"'<'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"SKIPSTATEMENT", 
                      u"ALLOC", u"IF", u"THEN", u"ELSE", u"DONE", u"WHILE", 
                      u"DO", u"OD", u"NULL", u"VAR", u"INT", u"PLUS", u"MINUS", 
                      u"MULTIPLY", u"DIVISION", u"EQUALS", u"LEQ", u"WHITESPACE" ]

    RULE_variable = 0
    RULE_statement = 1
    RULE_program = 2

    ruleNames =  [ u"variable", u"statement", u"program" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    SKIPSTATEMENT=7
    ALLOC=8
    IF=9
    THEN=10
    ELSE=11
    DONE=12
    WHILE=13
    DO=14
    OD=15
    NULL=16
    VAR=17
    INT=18
    PLUS=19
    MINUS=20
    MULTIPLY=21
    DIVISION=22
    EQUALS=23
    LEQ=24
    WHITESPACE=25

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


    class NullvarContext(VariableContext):

        def __init__(self, parser, ctx): # actually a pointersParser.VariableContext)
            super(pointersParser.NullvarContext, self).__init__(parser)
            self.copyFrom(ctx)

        def NULL(self):
            return self.getToken(pointersParser.NULL, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterNullvar"):
                listener.enterNullvar(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNullvar"):
                listener.exitNullvar(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitNullvar"):
                return visitor.visitNullvar(self)
            else:
                return visitor.visitChildren(self)



    def variable(self):

        localctx = pointersParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_variable)
        try:
            self.state = 8
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pointersParser.VAR]:
                localctx = pointersParser.VariableNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.match(pointersParser.VAR)
                pass
            elif token in [pointersParser.NULL]:
                localctx = pointersParser.NullvarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 7
                self.match(pointersParser.NULL)
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


    class AllocContext(StatementContext):

        def __init__(self, parser, ctx): # actually a pointersParser.StatementContext)
            super(pointersParser.AllocContext, self).__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(pointersParser.VariableContext,0)

        def ALLOC(self):
            return self.getToken(pointersParser.ALLOC, 0)
        def VAR(self):
            return self.getToken(pointersParser.VAR, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterAlloc"):
                listener.enterAlloc(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAlloc"):
                listener.exitAlloc(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitAlloc"):
                return visitor.visitAlloc(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(StatementContext):

        def __init__(self, parser, ctx): # actually a pointersParser.StatementContext)
            super(pointersParser.WhileContext, self).__init__(parser)
            self.cond = None # VariableContext
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(pointersParser.WHILE, 0)
        def variable(self):
            return self.getTypedRuleContext(pointersParser.VariableContext,0)

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
            self.cond = None # VariableContext
            self._statement = None # StatementContext
            self.ifs = list() # of StatementContexts
            self.elses = list() # of StatementContexts
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(pointersParser.IF, 0)
        def variable(self):
            return self.getTypedRuleContext(pointersParser.VariableContext,0)

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

        def variable(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(pointersParser.VariableContext)
            else:
                return self.getTypedRuleContext(pointersParser.VariableContext,i)


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
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = pointersParser.SkipContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.match(pointersParser.SKIPSTATEMENT)
                pass

            elif la_ == 2:
                localctx = pointersParser.AllocContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.variable()
                self.state = 12
                self.match(pointersParser.T__0)
                self.state = 13
                self.match(pointersParser.ALLOC)
                self.state = 14
                self.match(pointersParser.VAR)
                pass

            elif la_ == 3:
                localctx = pointersParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 16
                self.variable()
                self.state = 17
                self.match(pointersParser.T__0)
                self.state = 18
                self.variable()
                pass

            elif la_ == 4:
                localctx = pointersParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 20
                self.match(pointersParser.IF)
                self.state = 21
                self.match(pointersParser.T__1)
                self.state = 22
                localctx.cond = self.variable()
                self.state = 23
                self.match(pointersParser.T__2)
                self.state = 24
                self.match(pointersParser.T__3)
                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 25
                    localctx._statement = self.statement()
                    localctx.ifs.append(localctx._statement)
                    self.state = 26
                    self.match(pointersParser.T__4)
                    self.state = 30 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pointersParser.SKIPSTATEMENT) | (1 << pointersParser.IF) | (1 << pointersParser.WHILE) | (1 << pointersParser.NULL) | (1 << pointersParser.VAR))) != 0)):
                        break

                self.state = 32
                self.match(pointersParser.T__5)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==pointersParser.ELSE:
                    self.state = 33
                    self.match(pointersParser.ELSE)
                    self.state = 34
                    self.match(pointersParser.T__3)
                    self.state = 38 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 35
                        localctx._statement = self.statement()
                        localctx.elses.append(localctx._statement)
                        self.state = 36
                        self.match(pointersParser.T__4)
                        self.state = 40 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pointersParser.SKIPSTATEMENT) | (1 << pointersParser.IF) | (1 << pointersParser.WHILE) | (1 << pointersParser.NULL) | (1 << pointersParser.VAR))) != 0)):
                            break

                    self.state = 42
                    self.match(pointersParser.T__5)


                pass

            elif la_ == 5:
                localctx = pointersParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 46
                self.match(pointersParser.WHILE)
                self.state = 47
                self.match(pointersParser.T__1)
                self.state = 48
                localctx.cond = self.variable()
                self.state = 49
                self.match(pointersParser.T__2)
                self.state = 50
                self.match(pointersParser.T__3)
                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 51
                    self.statement()
                    self.state = 52
                    self.match(pointersParser.T__4)
                    self.state = 56 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pointersParser.SKIPSTATEMENT) | (1 << pointersParser.IF) | (1 << pointersParser.WHILE) | (1 << pointersParser.NULL) | (1 << pointersParser.VAR))) != 0)):
                        break

                self.state = 58
                self.match(pointersParser.T__5)
                pass


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
        self.enterRule(localctx, 4, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self.statement()
                self.state = 63
                self.match(pointersParser.T__4)
                self.state = 67 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pointersParser.SKIPSTATEMENT) | (1 << pointersParser.IF) | (1 << pointersParser.WHILE) | (1 << pointersParser.NULL) | (1 << pointersParser.VAR))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





