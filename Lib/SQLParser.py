#! /usr/bin/env python
# coding: utf-8

from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\u00ce\u06ae\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write(u"\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4")
        buf.write(u"\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t")
        buf.write(u"\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27")
        buf.write(u"\4\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4")
        buf.write(u"\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t")
        buf.write(u"#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4")
        buf.write(u",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62")
        buf.write(u"\4\63\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\4")
        buf.write(u"8\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@")
        buf.write(u"\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\t")
        buf.write(u"I\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R")
        buf.write(u"\tR\4S\tS\4T\tT\4U\tU\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4")
        buf.write(u"[\t[\4\\\t\\\4]\t]\4^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\t")
        buf.write(u"c\4d\td\4e\te\4f\tf\4g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l")
        buf.write(u"\tl\4m\tm\4n\tn\4o\to\4p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4")
        buf.write(u"u\tu\4v\tv\4w\tw\4x\tx\4y\ty\4z\tz\4{\t{\4|\t|\4}\t}")
        buf.write(u"\4~\t~\4\177\t\177\4\u0080\t\u0080\4\u0081\t\u0081\4")
        buf.write(u"\u0082\t\u0082\4\u0083\t\u0083\4\u0084\t\u0084\4\u0085")
        buf.write(u"\t\u0085\4\u0086\t\u0086\4\u0087\t\u0087\4\u0088\t\u0088")
        buf.write(u"\4\u0089\t\u0089\4\u008a\t\u008a\4\u008b\t\u008b\4\u008c")
        buf.write(u"\t\u008c\4\u008d\t\u008d\4\u008e\t\u008e\4\u008f\t\u008f")
        buf.write(u"\4\u0090\t\u0090\4\u0091\t\u0091\4\u0092\t\u0092\4\u0093")
        buf.write(u"\t\u0093\4\u0094\t\u0094\4\u0095\t\u0095\4\u0096\t\u0096")
        buf.write(u"\4\u0097\t\u0097\4\u0098\t\u0098\4\u0099\t\u0099\4\u009a")
        buf.write(u"\t\u009a\4\u009b\t\u009b\4\u009c\t\u009c\4\u009d\t\u009d")
        buf.write(u"\4\u009e\t\u009e\4\u009f\t\u009f\4\u00a0\t\u00a0\4\u00a1")
        buf.write(u"\t\u00a1\4\u00a2\t\u00a2\4\u00a3\t\u00a3\4\u00a4\t\u00a4")
        buf.write(u"\4\u00a5\t\u00a5\4\u00a6\t\u00a6\4\u00a7\t\u00a7\4\u00a8")
        buf.write(u"\t\u00a8\4\u00a9\t\u00a9\4\u00aa\t\u00aa\4\u00ab\t\u00ab")
        buf.write(u"\4\u00ac\t\u00ac\4\u00ad\t\u00ad\4\u00ae\t\u00ae\4\u00af")
        buf.write(u"\t\u00af\4\u00b0\t\u00b0\4\u00b1\t\u00b1\4\u00b2\t\u00b2")
        buf.write(u"\4\u00b3\t\u00b3\4\u00b4\t\u00b4\4\u00b5\t\u00b5\4\u00b6")
        buf.write(u"\t\u00b6\4\u00b7\t\u00b7\4\u00b8\t\u00b8\4\u00b9\t\u00b9")
        buf.write(u"\4\u00ba\t\u00ba\4\u00bb\t\u00bb\4\u00bc\t\u00bc\4\u00bd")
        buf.write(u"\t\u00bd\4\u00be\t\u00be\4\u00bf\t\u00bf\4\u00c0\t\u00c0")
        buf.write(u"\4\u00c1\t\u00c1\4\u00c2\t\u00c2\4\u00c3\t\u00c3\4\u00c4")
        buf.write(u"\t\u00c4\4\u00c5\t\u00c5\4\u00c6\t\u00c6\4\u00c7\t\u00c7")
        buf.write(u"\4\u00c8\t\u00c8\4\u00c9\t\u00c9\4\u00ca\t\u00ca\3\2")
        buf.write(u"\3\2\5\2\u0197\n\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u019f")
        buf.write(u"\n\3\3\4\3\4\3\5\3\5\3\6\3\6\5\6\u01a7\n\6\3\7\3\7\5")
        buf.write(u"\7\u01ab\n\7\3\7\3\7\3\7\3\7\3\7\5\7\u01b2\n\7\3\7\3")
        buf.write(u"\7\3\7\3\7\5\7\u01b8\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write(u"\3\b\5\b\u01c2\n\b\3\b\5\b\u01c5\n\b\3\b\3\b\3\b\3\b")
        buf.write(u"\3\b\3\b\3\b\3\b\3\b\5\b\u01d0\n\b\3\b\5\b\u01d3\n\b")
        buf.write(u"\3\b\5\b\u01d6\n\b\3\b\3\b\5\b\u01da\n\b\3\b\3\b\3\b")
        buf.write(u"\3\b\3\b\5\b\u01e1\n\b\3\b\5\b\u01e4\n\b\3\b\5\b\u01e7")
        buf.write(u"\n\b\3\b\3\b\3\b\5\b\u01ec\n\b\3\t\3\t\3\t\3\t\7\t\u01f2")
        buf.write(u"\n\t\f\t\16\t\u01f5\13\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13")
        buf.write(u"\3\f\3\f\3\f\3\f\3\f\7\f\u0203\n\f\f\f\16\f\u0206\13")
        buf.write(u"\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3")
        buf.write(u"\17\3\20\3\20\3\21\3\21\3\21\3\21\5\21\u021a\n\21\3\22")
        buf.write(u"\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3")
        buf.write(u"\23\3\23\7\23\u0229\n\23\f\23\16\23\u022c\13\23\3\24")
        buf.write(u"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0238")
        buf.write(u"\n\24\3\24\3\24\5\24\u023c\n\24\5\24\u023e\n\24\3\25")
        buf.write(u"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5")
        buf.write(u"\25\u024b\n\25\3\26\3\26\3\26\7\26\u0250\n\26\f\26\16")
        buf.write(u"\26\u0253\13\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3")
        buf.write(u"\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write(u"\3\32\7\32\u0268\n\32\f\32\16\32\u026b\13\32\3\33\3\33")
        buf.write(u"\3\33\3\33\5\33\u0271\n\33\3\33\3\33\3\33\3\33\3\34\3")
        buf.write(u"\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\36\5\36")
        buf.write(u"\u0282\n\36\3\37\3\37\5\37\u0286\n\37\3 \3 \3!\3!\5!")
        buf.write(u"\u028c\n!\3\"\3\"\3\"\5\"\u0291\n\"\3#\3#\3#\5#\u0296")
        buf.write(u"\n#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3")
        buf.write(u")\3)\3)\3)\3)\3)\3)\5)\u02ae\n)\3*\3*\3+\3+\5+\u02b4")
        buf.write(u"\n+\3+\3+\5+\u02b8\n+\3+\3+\3+\5+\u02bd\n+\3+\3+\3+\5")
        buf.write(u"+\u02c2\n+\3+\3+\5+\u02c6\n+\3+\5+\u02c9\n+\3,\3,\3,")
        buf.write(u"\3,\3-\3-\3-\5-\u02d2\n-\3-\3-\3-\5-\u02d7\n-\3-\3-\5")
        buf.write(u"-\u02db\n-\3-\3-\3-\3-\5-\u02e1\n-\3-\3-\3-\3-\5-\u02e7")
        buf.write(u"\n-\3-\3-\3-\5-\u02ec\n-\3-\3-\5-\u02f0\n-\5-\u02f2\n")
        buf.write(u"-\3.\3.\5.\u02f6\n.\3.\3.\5.\u02fa\n.\5.\u02fc\n.\3/")
        buf.write(u"\3/\5/\u0300\n/\3\60\3\60\5\60\u0304\n\60\3\60\3\60\5")
        buf.write(u"\60\u0308\n\60\3\60\3\60\5\60\u030c\n\60\3\60\3\60\3")
        buf.write(u"\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u0317\n\60\3\61")
        buf.write(u"\3\61\5\61\u031b\n\61\3\61\3\61\3\61\3\61\3\61\3\61\5")
        buf.write(u"\61\u0323\n\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write(u"\5\62\u032d\n\62\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3")
        buf.write(u"\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u033e\n\64")
        buf.write(u"\3\65\3\65\5\65\u0342\n\65\3\65\3\65\5\65\u0346\n\65")
        buf.write(u"\3\65\3\65\3\65\5\65\u034b\n\65\5\65\u034d\n\65\3\66")
        buf.write(u"\3\66\5\66\u0351\n\66\3\66\3\66\3\66\5\66\u0356\n\66")
        buf.write(u"\3\66\3\66\5\66\u035a\n\66\5\66\u035c\n\66\3\67\3\67")
        buf.write(u"\5\67\u0360\n\67\38\38\38\38\39\39\39\39\39\39\39\59")
        buf.write(u"\u036d\n9\3:\3:\3;\3;\3<\5<\u0374\n<\3<\3<\3=\3=\3>\3")
        buf.write(u">\3>\3>\3>\3>\5>\u0380\n>\5>\u0382\n>\3?\3?\3?\5?\u0387")
        buf.write(u"\n?\3?\3?\3?\3@\3@\3A\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3")
        buf.write(u"C\3C\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\6D\u03a7\nD")
        buf.write(u"\rD\16D\u03a8\3D\3D\5D\u03ad\nD\3E\3E\5E\u03b1\nE\3F")
        buf.write(u"\3F\3F\6F\u03b6\nF\rF\16F\u03b7\3F\5F\u03bb\nF\3F\3F")
        buf.write(u"\3G\3G\6G\u03c1\nG\rG\16G\u03c2\3G\5G\u03c6\nG\3G\3G")
        buf.write(u"\3H\3H\3H\3H\3H\3I\3I\3I\3I\3I\3J\3J\3J\3K\3K\5K\u03d9")
        buf.write(u"\nK\3L\3L\3L\3L\3L\3L\3L\3M\3M\3N\3N\3O\3O\3O\5O\u03e9")
        buf.write(u"\nO\3P\3P\3P\5P\u03ee\nP\3Q\3Q\3Q\7Q\u03f3\nQ\fQ\16Q")
        buf.write(u"\u03f6\13Q\3R\3R\3R\7R\u03fb\nR\fR\16R\u03fe\13R\3S\5")
        buf.write(u"S\u0401\nS\3S\3S\3T\3T\3T\3T\7T\u0409\nT\fT\16T\u040c")
        buf.write(u"\13T\3T\3T\3U\3U\3U\7U\u0413\nU\fU\16U\u0416\13U\3U\5")
        buf.write(u"U\u0419\nU\3V\3V\3W\3W\3X\3X\3X\3X\3X\3X\3X\3Y\3Y\3Y")
        buf.write(u"\5Y\u0429\nY\3Z\3Z\3[\3[\5[\u042f\n[\3\\\3\\\3]\3]\3")
        buf.write(u"]\7]\u0436\n]\f]\16]\u0439\13]\3^\3^\3_\3_\5_\u043f\n")
        buf.write(u"_\3`\3`\3a\3a\3a\3a\3a\3b\5b\u0449\nb\3b\5b\u044c\nb")
        buf.write(u"\3b\5b\u044f\nb\3b\3b\3b\3b\3b\5b\u0456\nb\3c\3c\3d\3")
        buf.write(u"d\3e\3e\3e\7e\u045f\ne\fe\16e\u0462\13e\3f\3f\3f\7f\u0467")
        buf.write(u"\nf\ff\16f\u046a\13f\3g\3g\3g\5g\u046f\ng\3h\3h\5h\u0473")
        buf.write(u"\nh\3i\3i\5i\u0477\ni\3i\3i\3j\3j\3k\3k\5k\u047f\nk\3")
        buf.write(u"l\3l\5l\u0483\nl\3m\3m\3m\3m\3n\3n\5n\u048b\nn\3o\3o")
        buf.write(u"\3p\3p\3q\3q\5q\u0493\nq\3r\3r\5r\u0497\nr\3s\3s\5s\u049b")
        buf.write(u"\ns\3s\5s\u049e\ns\3s\5s\u04a1\ns\3s\5s\u04a4\ns\3s\5")
        buf.write(u"s\u04a7\ns\3t\3t\3t\3u\3u\3u\7u\u04af\nu\fu\16u\u04b2")
        buf.write(u"\13u\3v\3v\5v\u04b6\nv\3w\3w\6w\u04ba\nw\rw\16w\u04bb")
        buf.write(u"\3x\3x\3x\3x\5x\u04c2\nx\3x\3x\3x\3x\3x\3x\5x\u04ca\n")
        buf.write(u"x\3x\3x\3x\3x\3x\5x\u04d1\nx\3y\3y\3y\3y\3z\5z\u04d8")
        buf.write(u"\nz\3z\3z\3z\3z\3{\3{\5{\u04e0\n{\3{\3{\3{\3|\3|\3|\3")
        buf.write(u"|\3}\3}\5}\u04eb\n}\3~\3~\5~\u04ef\n~\3\177\3\177\3\u0080")
        buf.write(u"\3\u0080\5\u0080\u04f5\n\u0080\3\u0081\3\u0081\3\u0081")
        buf.write(u"\3\u0082\3\u0082\3\u0082\3\u0082\3\u0082\3\u0083\3\u0083")
        buf.write(u"\5\u0083\u0501\n\u0083\3\u0083\5\u0083\u0504\n\u0083")
        buf.write(u"\3\u0083\3\u0083\3\u0083\3\u0083\5\u0083\u050a\n\u0083")
        buf.write(u"\3\u0083\3\u0083\5\u0083\u050e\n\u0083\3\u0083\3\u0083")
        buf.write(u"\3\u0083\3\u0083\3\u0083\5\u0083\u0515\n\u0083\5\u0083")
        buf.write(u"\u0517\n\u0083\3\u0084\3\u0084\3\u0084\7\u0084\u051c")
        buf.write(u"\n\u0084\f\u0084\16\u0084\u051f\13\u0084\3\u0085\3\u0085")
        buf.write(u"\3\u0086\3\u0086\3\u0086\3\u0087\3\u0087\3\u0088\3\u0088")
        buf.write(u"\3\u0088\3\u0088\3\u0089\3\u0089\3\u0089\7\u0089\u052f")
        buf.write(u"\n\u0089\f\u0089\16\u0089\u0532\13\u0089\3\u008a\3\u008a")
        buf.write(u"\3\u008a\3\u008a\5\u008a\u0538\n\u008a\3\u008b\3\u008b")
        buf.write(u"\3\u008b\3\u008b\3\u008b\5\u008b\u053f\n\u008b\3\u008c")
        buf.write(u"\3\u008c\3\u008c\7\u008c\u0544\n\u008c\f\u008c\16\u008c")
        buf.write(u"\u0547\13\u008c\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d")
        buf.write(u"\3\u008e\3\u008e\3\u008e\3\u008e\3\u008e\3\u008f\3\u008f")
        buf.write(u"\3\u008f\3\u0090\3\u0090\3\u0090\3\u0091\3\u0091\3\u0091")
        buf.write(u"\7\u0091\u055c\n\u0091\f\u0091\16\u0091\u055f\13\u0091")
        buf.write(u"\3\u0092\3\u0092\3\u0093\3\u0093\5\u0093\u0565\n\u0093")
        buf.write(u"\3\u0094\3\u0094\3\u0094\3\u0094\5\u0094\u056b\n\u0094")
        buf.write(u"\3\u0094\3\u0094\5\u0094\u056f\n\u0094\3\u0094\3\u0094")
        buf.write(u"\5\u0094\u0573\n\u0094\3\u0094\7\u0094\u0576\n\u0094")
        buf.write(u"\f\u0094\16\u0094\u0579\13\u0094\3\u0095\3\u0095\5\u0095")
        buf.write(u"\u057d\n\u0095\3\u0096\3\u0096\3\u0096\3\u0096\5\u0096")
        buf.write(u"\u0583\n\u0096\3\u0096\3\u0096\5\u0096\u0587\n\u0096")
        buf.write(u"\3\u0096\3\u0096\5\u0096\u058b\n\u0096\3\u0096\7\u0096")
        buf.write(u"\u058e\n\u0096\f\u0096\16\u0096\u0591\13\u0096\3\u0097")
        buf.write(u"\3\u0097\5\u0097\u0595\n\u0097\3\u0098\3\u0098\3\u0098")
        buf.write(u"\3\u0098\3\u0098\5\u0098\u059c\n\u0098\3\u0099\3\u0099")
        buf.write(u"\5\u0099\u05a0\n\u0099\3\u009a\3\u009a\3\u009a\3\u009b")
        buf.write(u"\3\u009b\5\u009b\u05a7\n\u009b\3\u009c\3\u009c\3\u009c")
        buf.write(u"\3\u009c\3\u009c\5\u009c\u05ae\n\u009c\5\u009c\u05b0")
        buf.write(u"\n\u009c\3\u009d\3\u009d\5\u009d\u05b4\n\u009d\3\u009d")
        buf.write(u"\3\u009d\5\u009d\u05b8\n\u009d\3\u009e\3\u009e\3\u009e")
        buf.write(u"\7\u009e\u05bd\n\u009e\f\u009e\16\u009e\u05c0\13\u009e")
        buf.write(u"\3\u009f\3\u009f\5\u009f\u05c4\n\u009f\3\u00a0\3\u00a0")
        buf.write(u"\5\u00a0\u05c8\n\u00a0\3\u00a1\3\u00a1\5\u00a1\u05cc")
        buf.write(u"\n\u00a1\3\u00a1\3\u00a1\3\u00a2\3\u00a2\3\u00a3\3\u00a3")
        buf.write(u"\3\u00a3\5\u00a3\u05d5\n\u00a3\3\u00a3\3\u00a3\3\u00a4")
        buf.write(u"\5\u00a4\u05da\n\u00a4\3\u00a4\3\u00a4\3\u00a5\3\u00a5")
        buf.write(u"\3\u00a5\7\u00a5\u05e1\n\u00a5\f\u00a5\16\u00a5\u05e4")
        buf.write(u"\13\u00a5\3\u00a6\3\u00a6\3\u00a7\3\u00a7\3\u00a8\3\u00a8")
        buf.write(u"\3\u00a9\3\u00a9\3\u00a9\3\u00a9\3\u00aa\3\u00aa\3\u00aa")
        buf.write(u"\3\u00aa\3\u00aa\3\u00aa\5\u00aa\u05f6\n\u00aa\3\u00ab")
        buf.write(u"\3\u00ab\3\u00ab\3\u00ab\3\u00ac\3\u00ac\3\u00ad\3\u00ad")
        buf.write(u"\3\u00ad\3\u00ae\5\u00ae\u0602\n\u00ae\3\u00ae\3\u00ae")
        buf.write(u"\5\u00ae\u0606\n\u00ae\3\u00ae\3\u00ae\3\u00ae\3\u00ae")
        buf.write(u"\3\u00af\3\u00af\5\u00af\u060e\n\u00af\3\u00af\3\u00af")
        buf.write(u"\3\u00af\3\u00b0\3\u00b0\3\u00b0\3\u00b0\3\u00b0\5\u00b0")
        buf.write(u"\u0618\n\u00b0\3\u00b1\3\u00b1\3\u00b1\7\u00b1\u061d")
        buf.write(u"\n\u00b1\f\u00b1\16\u00b1\u0620\13\u00b1\3\u00b2\3\u00b2")
        buf.write(u"\3\u00b2\3\u00b2\3\u00b3\5\u00b3\u0627\n\u00b3\3\u00b3")
        buf.write(u"\3\u00b3\5\u00b3\u062b\n\u00b3\3\u00b4\3\u00b4\3\u00b4")
        buf.write(u"\3\u00b4\3\u00b4\3\u00b4\5\u00b4\u0633\n\u00b4\3\u00b5")
        buf.write(u"\3\u00b5\3\u00b6\3\u00b6\3\u00b6\5\u00b6\u063a\n\u00b6")
        buf.write(u"\3\u00b6\3\u00b6\3\u00b7\3\u00b7\3\u00b7\3\u00b7\3\u00b7")
        buf.write(u"\3\u00b8\3\u00b8\5\u00b8\u0645\n\u00b8\3\u00b9\3\u00b9")
        buf.write(u"\3\u00ba\3\u00ba\3\u00bb\5\u00bb\u064c\n\u00bb\3\u00bb")
        buf.write(u"\3\u00bb\3\u00bb\3\u00bc\3\u00bc\3\u00bc\3\u00bd\3\u00bd")
        buf.write(u"\5\u00bd\u0656\n\u00bd\3\u00be\3\u00be\3\u00bf\3\u00bf")
        buf.write(u"\3\u00c0\3\u00c0\3\u00c0\5\u00c0\u065f\n\u00c0\3\u00c0")
        buf.write(u"\3\u00c0\3\u00c1\3\u00c1\3\u00c2\3\u00c2\5\u00c2\u0667")
        buf.write(u"\n\u00c2\3\u00c3\3\u00c3\3\u00c3\7\u00c3\u066c\n\u00c3")
        buf.write(u"\f\u00c3\16\u00c3\u066f\13\u00c3\3\u00c4\3\u00c4\3\u00c4")
        buf.write(u"\3\u00c4\3\u00c5\3\u00c5\3\u00c5\7\u00c5\u0678\n\u00c5")
        buf.write(u"\f\u00c5\16\u00c5\u067b\13\u00c5\3\u00c6\3\u00c6\5\u00c6")
        buf.write(u"\u067f\n\u00c6\3\u00c6\5\u00c6\u0682\n\u00c6\3\u00c7")
        buf.write(u"\3\u00c7\3\u00c8\3\u00c8\3\u00c8\3\u00c9\3\u00c9\3\u00c9")
        buf.write(u"\3\u00c9\5\u00c9\u068d\n\u00c9\3\u00ca\3\u00ca\5\u00ca")
        buf.write(u"\u0691\n\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca")
        buf.write(u"\3\u00ca\5\u00ca\u0699\n\u00ca\3\u00ca\3\u00ca\3\u00ca")
        buf.write(u"\3\u00ca\5\u00ca\u069f\n\u00ca\3\u00ca\3\u00ca\3\u00ca")
        buf.write(u"\3\u00ca\3\u00ca\3\u00ca\5\u00ca\u06a7\n\u00ca\5\u00ca")
        buf.write(u"\u06a9\n\u00ca\3\u00ca\5\u00ca\u06ac\n\u00ca\3\u00ca")
        buf.write(u"\2\2\u00cb\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write(u"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvx")
        buf.write(u"z|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090")
        buf.write(u"\u0092\u0094\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2")
        buf.write(u"\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4")
        buf.write(u"\u00b6\u00b8\u00ba\u00bc\u00be\u00c0\u00c2\u00c4\u00c6")
        buf.write(u"\u00c8\u00ca\u00cc\u00ce\u00d0\u00d2\u00d4\u00d6\u00d8")
        buf.write(u"\u00da\u00dc\u00de\u00e0\u00e2\u00e4\u00e6\u00e8\u00ea")
        buf.write(u"\u00ec\u00ee\u00f0\u00f2\u00f4\u00f6\u00f8\u00fa\u00fc")
        buf.write(u"\u00fe\u0100\u0102\u0104\u0106\u0108\u010a\u010c\u010e")
        buf.write(u"\u0110\u0112\u0114\u0116\u0118\u011a\u011c\u011e\u0120")
        buf.write(u"\u0122\u0124\u0126\u0128\u012a\u012c\u012e\u0130\u0132")
        buf.write(u"\u0134\u0136\u0138\u013a\u013c\u013e\u0140\u0142\u0144")
        buf.write(u"\u0146\u0148\u014a\u014c\u014e\u0150\u0152\u0154\u0156")
        buf.write(u"\u0158\u015a\u015c\u015e\u0160\u0162\u0164\u0166\u0168")
        buf.write(u"\u016a\u016c\u016e\u0170\u0172\u0174\u0176\u0178\u017a")
        buf.write(u"\u017c\u017e\u0180\u0182\u0184\u0186\u0188\u018a\u018c")
        buf.write(u"\u018e\u0190\u0192\2\26\5\28RT\u00a4\u00a6\u00a9\5\2")
        buf.write(u"\23\23\61\61\177\177\3\2\u0087\u0088\3\2\u00c6\u00c7")
        buf.write(u"\17\2\6\6,,88==@@IIPPVV]]bbtuww\u0081\u0082\3\2\u00bc")
        buf.write(u"\u00bd\3\2\u00be\u00c0\3\2z|\5\2\t\t\37\37\60\60\5\2")
        buf.write(u"\24\24  **\4\2\22\22\62\62\4\2\4\4\17\17\4\2\u00b0\u00b0")
        buf.write(u"\u00b5\u00b9\4\2\7\7--\3\2\u00aa\u00ad\4\2\6\6,,\6\2")
        buf.write(u"BBSScd\u0085\u0085\t\2;;DFHHWX_all\u0084\u0084\4\2  ")
        buf.write(u"**\4\2\b\b\16\16\2\u06dd\2\u0194\3\2\2\2\4\u019e\3\2")
        buf.write(u"\2\2\6\u01a0\3\2\2\2\b\u01a2\3\2\2\2\n\u01a6\3\2\2\2")
        buf.write(u"\f\u01a8\3\2\2\2\16\u01eb\3\2\2\2\20\u01ed\3\2\2\2\22")
        buf.write(u"\u01f8\3\2\2\2\24\u01fb\3\2\2\2\26\u01fd\3\2\2\2\30\u0209")
        buf.write(u"\3\2\2\2\32\u020d\3\2\2\2\34\u0210\3\2\2\2\36\u0213\3")
        buf.write(u"\2\2\2 \u0219\3\2\2\2\"\u021b\3\2\2\2$\u0225\3\2\2\2")
        buf.write(u"&\u022d\3\2\2\2(\u023f\3\2\2\2*\u024c\3\2\2\2,\u0254")
        buf.write(u"\3\2\2\2.\u0257\3\2\2\2\60\u025a\3\2\2\2\62\u0264\3\2")
        buf.write(u"\2\2\64\u026c\3\2\2\2\66\u0276\3\2\2\28\u027b\3\2\2\2")
        buf.write(u":\u027d\3\2\2\2<\u0285\3\2\2\2>\u0287\3\2\2\2@\u028b")
        buf.write(u"\3\2\2\2B\u0290\3\2\2\2D\u0295\3\2\2\2F\u0297\3\2\2\2")
        buf.write(u"H\u029a\3\2\2\2J\u029d\3\2\2\2L\u02a0\3\2\2\2N\u02a2")
        buf.write(u"\3\2\2\2P\u02ad\3\2\2\2R\u02af\3\2\2\2T\u02c8\3\2\2\2")
        buf.write(u"V\u02ca\3\2\2\2X\u02f1\3\2\2\2Z\u02fb\3\2\2\2\\\u02ff")
        buf.write(u"\3\2\2\2^\u0316\3\2\2\2`\u0322\3\2\2\2b\u032c\3\2\2\2")
        buf.write(u"d\u032e\3\2\2\2f\u033d\3\2\2\2h\u034c\3\2\2\2j\u035b")
        buf.write(u"\3\2\2\2l\u035f\3\2\2\2n\u0361\3\2\2\2p\u036c\3\2\2\2")
        buf.write(u"r\u036e\3\2\2\2t\u0370\3\2\2\2v\u0373\3\2\2\2x\u0377")
        buf.write(u"\3\2\2\2z\u0381\3\2\2\2|\u0383\3\2\2\2~\u038b\3\2\2\2")
        buf.write(u"\u0080\u038d\3\2\2\2\u0082\u0393\3\2\2\2\u0084\u0398")
        buf.write(u"\3\2\2\2\u0086\u03ac\3\2\2\2\u0088\u03b0\3\2\2\2\u008a")
        buf.write(u"\u03b2\3\2\2\2\u008c\u03be\3\2\2\2\u008e\u03c9\3\2\2")
        buf.write(u"\2\u0090\u03ce\3\2\2\2\u0092\u03d3\3\2\2\2\u0094\u03d8")
        buf.write(u"\3\2\2\2\u0096\u03da\3\2\2\2\u0098\u03e1\3\2\2\2\u009a")
        buf.write(u"\u03e3\3\2\2\2\u009c\u03e8\3\2\2\2\u009e\u03ed\3\2\2")
        buf.write(u"\2\u00a0\u03ef\3\2\2\2\u00a2\u03f7\3\2\2\2\u00a4\u0400")
        buf.write(u"\3\2\2\2\u00a6\u0404\3\2\2\2\u00a8\u0418\3\2\2\2\u00aa")
        buf.write(u"\u041a\3\2\2\2\u00ac\u041c\3\2\2\2\u00ae\u041e\3\2\2")
        buf.write(u"\2\u00b0\u0428\3\2\2\2\u00b2\u042a\3\2\2\2\u00b4\u042e")
        buf.write(u"\3\2\2\2\u00b6\u0430\3\2\2\2\u00b8\u0432\3\2\2\2\u00ba")
        buf.write(u"\u043a\3\2\2\2\u00bc\u043e\3\2\2\2\u00be\u0440\3\2\2")
        buf.write(u"\2\u00c0\u0442\3\2\2\2\u00c2\u0455\3\2\2\2\u00c4\u0457")
        buf.write(u"\3\2\2\2\u00c6\u0459\3\2\2\2\u00c8\u045b\3\2\2\2\u00ca")
        buf.write(u"\u0463\3\2\2\2\u00cc\u046e\3\2\2\2\u00ce\u0470\3\2\2")
        buf.write(u"\2\u00d0\u0474\3\2\2\2\u00d2\u047a\3\2\2\2\u00d4\u047e")
        buf.write(u"\3\2\2\2\u00d6\u0482\3\2\2\2\u00d8\u0484\3\2\2\2\u00da")
        buf.write(u"\u048a\3\2\2\2\u00dc\u048c\3\2\2\2\u00de\u048e\3\2\2")
        buf.write(u"\2\u00e0\u0492\3\2\2\2\u00e2\u0496\3\2\2\2\u00e4\u0498")
        buf.write(u"\3\2\2\2\u00e6\u04a8\3\2\2\2\u00e8\u04ab\3\2\2\2\u00ea")
        buf.write(u"\u04b5\3\2\2\2\u00ec\u04b7\3\2\2\2\u00ee\u04d0\3\2\2")
        buf.write(u"\2\u00f0\u04d2\3\2\2\2\u00f2\u04d7\3\2\2\2\u00f4\u04dd")
        buf.write(u"\3\2\2\2\u00f6\u04e4\3\2\2\2\u00f8\u04ea\3\2\2\2\u00fa")
        buf.write(u"\u04ec\3\2\2\2\u00fc\u04f0\3\2\2\2\u00fe\u04f4\3\2\2")
        buf.write(u"\2\u0100\u04f6\3\2\2\2\u0102\u04f9\3\2\2\2\u0104\u0516")
        buf.write(u"\3\2\2\2\u0106\u0518\3\2\2\2\u0108\u0520\3\2\2\2\u010a")
        buf.write(u"\u0522\3\2\2\2\u010c\u0525\3\2\2\2\u010e\u0527\3\2\2")
        buf.write(u"\2\u0110\u052b\3\2\2\2\u0112\u0537\3\2\2\2\u0114\u053e")
        buf.write(u"\3\2\2\2\u0116\u0540\3\2\2\2\u0118\u0548\3\2\2\2\u011a")
        buf.write(u"\u054d\3\2\2\2\u011c\u0552\3\2\2\2\u011e\u0555\3\2\2")
        buf.write(u"\2\u0120\u0558\3\2\2\2\u0122\u0560\3\2\2\2\u0124\u0564")
        buf.write(u"\3\2\2\2\u0126\u056e\3\2\2\2\u0128\u057c\3\2\2\2\u012a")
        buf.write(u"\u0586\3\2\2\2\u012c\u0594\3\2\2\2\u012e\u059b\3\2\2")
        buf.write(u"\2\u0130\u059f\3\2\2\2\u0132\u05a1\3\2\2\2\u0134\u05a6")
        buf.write(u"\3\2\2\2\u0136\u05a8\3\2\2\2\u0138\u05b1\3\2\2\2\u013a")
        buf.write(u"\u05b9\3\2\2\2\u013c\u05c3\3\2\2\2\u013e\u05c5\3\2\2")
        buf.write(u"\2\u0140\u05cb\3\2\2\2\u0142\u05cf\3\2\2\2\u0144\u05d4")
        buf.write(u"\3\2\2\2\u0146\u05d9\3\2\2\2\u0148\u05dd\3\2\2\2\u014a")
        buf.write(u"\u05e5\3\2\2\2\u014c\u05e7\3\2\2\2\u014e\u05e9\3\2\2")
        buf.write(u"\2\u0150\u05eb\3\2\2\2\u0152\u05f5\3\2\2\2\u0154\u05f7")
        buf.write(u"\3\2\2\2\u0156\u05fb\3\2\2\2\u0158\u05fd\3\2\2\2\u015a")
        buf.write(u"\u0601\3\2\2\2\u015c\u060b\3\2\2\2\u015e\u0617\3\2\2")
        buf.write(u"\2\u0160\u0619\3\2\2\2\u0162\u0621\3\2\2\2\u0164\u062a")
        buf.write(u"\3\2\2\2\u0166\u0632\3\2\2\2\u0168\u0634\3\2\2\2\u016a")
        buf.write(u"\u0636\3\2\2\2\u016c\u063d\3\2\2\2\u016e\u0644\3\2\2")
        buf.write(u"\2\u0170\u0646\3\2\2\2\u0172\u0648\3\2\2\2\u0174\u064b")
        buf.write(u"\3\2\2\2\u0176\u0650\3\2\2\2\u0178\u0655\3\2\2\2\u017a")
        buf.write(u"\u0657\3\2\2\2\u017c\u0659\3\2\2\2\u017e\u065b\3\2\2")
        buf.write(u"\2\u0180\u0662\3\2\2\2\u0182\u0666\3\2\2\2\u0184\u0668")
        buf.write(u"\3\2\2\2\u0186\u0670\3\2\2\2\u0188\u0674\3\2\2\2\u018a")
        buf.write(u"\u067c\3\2\2\2\u018c\u0683\3\2\2\2\u018e\u0685\3\2\2")
        buf.write(u"\2\u0190\u068c\3\2\2\2\u0192\u06ab\3\2\2\2\u0194\u0196")
        buf.write(u"\5\4\3\2\u0195\u0197\7\u00b2\2\2\u0196\u0195\3\2\2\2")
        buf.write(u"\u0196\u0197\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0199")
        buf.write(u"\7\2\2\3\u0199\3\3\2\2\2\u019a\u019f\5\6\4\2\u019b\u019f")
        buf.write(u"\5\b\5\2\u019c\u019f\5\n\6\2\u019d\u019f\5\f\7\2\u019e")
        buf.write(u"\u019a\3\2\2\2\u019e\u019b\3\2\2\2\u019e\u019c\3\2\2")
        buf.write(u"\2\u019e\u019d\3\2\2\2\u019f\5\3\2\2\2\u01a0\u01a1\5")
        buf.write(u"\u0122\u0092\2\u01a1\7\3\2\2\2\u01a2\u01a3\5\u0192\u00ca")
        buf.write(u"\2\u01a3\t\3\2\2\2\u01a4\u01a7\5\16\b\2\u01a5\u01a7\5")
        buf.write(u":\36\2\u01a6\u01a4\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7")
        buf.write(u"\13\3\2\2\2\u01a8\u01aa\7\f\2\2\u01a9\u01ab\7\63\2\2")
        buf.write(u"\u01aa\u01a9\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac")
        buf.write(u"\3\2\2\2\u01ac\u01ad\7T\2\2\u01ad\u01ae\5<\37\2\u01ae")
        buf.write(u"\u01af\7&\2\2\u01af\u01b1\5\u0136\u009c\2\u01b0\u01b2")
        buf.write(u"\5\32\16\2\u01b1\u01b0\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2")
        buf.write(u"\u01b3\3\2\2\2\u01b3\u01b4\7\u00ba\2\2\u01b4\u01b5\5")
        buf.write(u"\u0188\u00c5\2\u01b5\u01b7\7\u00bb\2\2\u01b6\u01b8\5")
        buf.write(u"\26\f\2\u01b7\u01b6\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8")
        buf.write(u"\r\3\2\2\2\u01b9\u01ba\7\f\2\2\u01ba\u01bb\7K\2\2\u01bb")
        buf.write(u"\u01bc\7.\2\2\u01bc\u01bd\5\u0136\u009c\2\u01bd\u01be")
        buf.write(u"\5\20\t\2\u01be\u01bf\7\64\2\2\u01bf\u01c1\5<\37\2\u01c0")
        buf.write(u"\u01c2\5\26\f\2\u01c1\u01c0\3\2\2\2\u01c1\u01c2\3\2\2")
        buf.write(u"\2\u01c2\u01c4\3\2\2\2\u01c3\u01c5\5 \21\2\u01c4\u01c3")
        buf.write(u"\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6")
        buf.write(u"\u01c7\7\\\2\2\u01c7\u01c8\7\u00cb\2\2\u01c8\u01ec\3")
        buf.write(u"\2\2\2\u01c9\u01ca\7\f\2\2\u01ca\u01cb\7.\2\2\u01cb\u01cc")
        buf.write(u"\5\u0136\u009c\2\u01cc\u01cf\5\20\t\2\u01cd\u01ce\7\64")
        buf.write(u"\2\2\u01ce\u01d0\5<\37\2\u01cf\u01cd\3\2\2\2\u01cf\u01d0")
        buf.write(u"\3\2\2\2\u01d0\u01d2\3\2\2\2\u01d1\u01d3\5\26\f\2\u01d2")
        buf.write(u"\u01d1\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d5\3\2\2")
        buf.write(u"\2\u01d4\u01d6\5 \21\2\u01d5\u01d4\3\2\2\2\u01d5\u01d6")
        buf.write(u"\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d8\7\3\2\2\u01d8")
        buf.write(u"\u01da\5\u0122\u0092\2\u01d9\u01d7\3\2\2\2\u01d9\u01da")
        buf.write(u"\3\2\2\2\u01da\u01ec\3\2\2\2\u01db\u01dc\7\f\2\2\u01dc")
        buf.write(u"\u01dd\7.\2\2\u01dd\u01e0\5\u0136\u009c\2\u01de\u01df")
        buf.write(u"\7\64\2\2\u01df\u01e1\5<\37\2\u01e0\u01de\3\2\2\2\u01e0")
        buf.write(u"\u01e1\3\2\2\2\u01e1\u01e3\3\2\2\2\u01e2\u01e4\5\26\f")
        buf.write(u"\2\u01e3\u01e2\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e6")
        buf.write(u"\3\2\2\2\u01e5\u01e7\5 \21\2\u01e6\u01e5\3\2\2\2\u01e6")
        buf.write(u"\u01e7\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01e9\7\3\2")
        buf.write(u"\2\u01e9\u01ea\5\u0122\u0092\2\u01ea\u01ec\3\2\2\2\u01eb")
        buf.write(u"\u01b9\3\2\2\2\u01eb\u01c9\3\2\2\2\u01eb\u01db\3\2\2")
        buf.write(u"\2\u01ec\17\3\2\2\2\u01ed\u01ee\7\u00ba\2\2\u01ee\u01f3")
        buf.write(u"\5\22\n\2\u01ef\u01f0\7\u00b3\2\2\u01f0\u01f2\5\22\n")
        buf.write(u"\2\u01f1\u01ef\3\2\2\2\u01f2\u01f5\3\2\2\2\u01f3\u01f1")
        buf.write(u"\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f6\3\2\2\2\u01f5")
        buf.write(u"\u01f3\3\2\2\2\u01f6\u01f7\7\u00bb\2\2\u01f7\21\3\2\2")
        buf.write(u"\2\u01f8\u01f9\5<\37\2\u01f9\u01fa\5\24\13\2\u01fa\23")
        buf.write(u"\3\2\2\2\u01fb\u01fc\5N(\2\u01fc\25\3\2\2\2\u01fd\u01fe")
        buf.write(u"\7\67\2\2\u01fe\u01ff\7\u00ba\2\2\u01ff\u0204\5\30\r")
        buf.write(u"\2\u0200\u0201\7\u00b3\2\2\u0201\u0203\5\30\r\2\u0202")
        buf.write(u"\u0200\3\2\2\2\u0203\u0206\3\2\2\2\u0204\u0202\3\2\2")
        buf.write(u"\2\u0204\u0205\3\2\2\2\u0205\u0207\3\2\2\2\u0206\u0204")
        buf.write(u"\3\2\2\2\u0207\u0208\7\u00bb\2\2\u0208\27\3\2\2\2\u0209")
        buf.write(u"\u020a\7\u00cb\2\2\u020a\u020b\7\u00b0\2\2\u020b\u020c")
        buf.write(u"\5\u00a0Q\2\u020c\31\3\2\2\2\u020d\u020e\7\64\2\2\u020e")
        buf.write(u"\u020f\5<\37\2\u020f\33\3\2\2\2\u0210\u0211\7x\2\2\u0211")
        buf.write(u"\u0212\5\36\20\2\u0212\35\3\2\2\2\u0213\u0214\5<\37\2")
        buf.write(u"\u0214\37\3\2\2\2\u0215\u021a\5\"\22\2\u0216\u021a\5")
        buf.write(u"(\25\2\u0217\u021a\5\60\31\2\u0218\u021a\5\66\34\2\u0219")
        buf.write(u"\u0215\3\2\2\2\u0219\u0216\3\2\2\2\u0219\u0217\3\2\2")
        buf.write(u"\2\u0219\u0218\3\2\2\2\u021a!\3\2\2\2\u021b\u021c\7h")
        buf.write(u"\2\2\u021c\u021d\7:\2\2\u021d\u021e\7m\2\2\u021e\u021f")
        buf.write(u"\7\u00ba\2\2\u021f\u0220\5\u0148\u00a5\2\u0220\u0221")
        buf.write(u"\7\u00bb\2\2\u0221\u0222\7\u00ba\2\2\u0222\u0223\5$\23")
        buf.write(u"\2\u0223\u0224\7\u00bb\2\2\u0224#\3\2\2\2\u0225\u022a")
        buf.write(u"\5&\24\2\u0226\u0227\7\u00b3\2\2\u0227\u0229\5&\24\2")
        buf.write(u"\u0228\u0226\3\2\2\2\u0229\u022c\3\2\2\2\u022a\u0228")
        buf.write(u"\3\2\2\2\u022a\u022b\3\2\2\2\u022b%\3\2\2\2\u022c\u022a")
        buf.write(u"\3\2\2\2\u022d\u022e\7h\2\2\u022e\u022f\58\35\2\u022f")
        buf.write(u"\u0230\7\u0080\2\2\u0230\u0231\7Z\2\2\u0231\u023d\7y")
        buf.write(u"\2\2\u0232\u0233\7\u00ba\2\2\u0233\u0234\5\u009cO\2\u0234")
        buf.write(u"\u0235\7\u00bb\2\2\u0235\u023e\3\2\2\2\u0236\u0238\7")
        buf.write(u"\u00ba\2\2\u0237\u0236\3\2\2\2\u0237\u0238\3\2\2\2\u0238")
        buf.write(u"\u0239\3\2\2\2\u0239\u023b\7^\2\2\u023a\u023c\7\u00bb")
        buf.write(u"\2\2\u023b\u023a\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u023e")
        buf.write(u"\3\2\2\2\u023d\u0232\3\2\2\2\u023d\u0237\3\2\2\2\u023e")
        buf.write(u"\'\3\2\2\2\u023f\u0240\7h\2\2\u0240\u0241\7:\2\2\u0241")
        buf.write(u"\u0242\7R\2\2\u0242\u0243\7\u00ba\2\2\u0243\u0244\5\u0148")
        buf.write(u"\u00a5\2\u0244\u024a\7\u00bb\2\2\u0245\u0246\7\u00ba")
        buf.write(u"\2\2\u0246\u0247\5*\26\2\u0247\u0248\7\u00bb\2\2\u0248")
        buf.write(u"\u024b\3\2\2\2\u0249\u024b\5.\30\2\u024a\u0245\3\2\2")
        buf.write(u"\2\u024a\u0249\3\2\2\2\u024b)\3\2\2\2\u024c\u0251\5,")
        buf.write(u"\27\2\u024d\u024e\7\u00b3\2\2\u024e\u0250\5,\27\2\u024f")
        buf.write(u"\u024d\3\2\2\2\u0250\u0253\3\2\2\2\u0251\u024f\3\2\2")
        buf.write(u"\2\u0251\u0252\3\2\2\2\u0252+\3\2\2\2\u0253\u0251\3\2")
        buf.write(u"\2\2\u0254\u0255\7h\2\2\u0255\u0256\58\35\2\u0256-\3")
        buf.write(u"\2\2\2\u0257\u0258\7i\2\2\u0258\u0259\5\u00a0Q\2\u0259")
        buf.write(u"/\3\2\2\2\u025a\u025b\7h\2\2\u025b\u025c\7:\2\2\u025c")
        buf.write(u"\u025d\7[\2\2\u025d\u025e\7\u00ba\2\2\u025e\u025f\5\u0148")
        buf.write(u"\u00a5\2\u025f\u0260\7\u00bb\2\2\u0260\u0261\7\u00ba")
        buf.write(u"\2\2\u0261\u0262\5\62\32\2\u0262\u0263\7\u00bb\2\2\u0263")
        buf.write(u"\61\3\2\2\2\u0264\u0269\5\64\33\2\u0265\u0266\7\u00b3")
        buf.write(u"\2\2\u0266\u0268\5\64\33\2\u0267\u0265\3\2\2\2\u0268")
        buf.write(u"\u026b\3\2\2\2\u0269\u0267\3\2\2\2\u0269\u026a\3\2\2")
        buf.write(u"\2\u026a\63\3\2\2\2\u026b\u0269\3\2\2\2\u026c\u026d\7")
        buf.write(u"h\2\2\u026d\u026e\58\35\2\u026e\u0270\7\u0080\2\2\u026f")
        buf.write(u"\u0271\7\31\2\2\u0270\u026f\3\2\2\2\u0270\u0271\3\2\2")
        buf.write(u"\2\u0271\u0272\3\2\2\2\u0272\u0273\7\u00ba\2\2\u0273")
        buf.write(u"\u0274\5\u0160\u00b1\2\u0274\u0275\7\u00bb\2\2\u0275")
        buf.write(u"\65\3\2\2\2\u0276\u0277\7h\2\2\u0277\u0278\7:\2\2\u0278")
        buf.write(u"\u0279\7?\2\2\u0279\u027a\5\20\t\2\u027a\67\3\2\2\2\u027b")
        buf.write(u"\u027c\5<\37\2\u027c9\3\2\2\2\u027d\u027e\7G\2\2\u027e")
        buf.write(u"\u027f\7.\2\2\u027f\u0281\5\u0136\u009c\2\u0280\u0282")
        buf.write(u"\7k\2\2\u0281\u0280\3\2\2\2\u0281\u0282\3\2\2\2\u0282")
        buf.write(u";\3\2\2\2\u0283\u0286\7\u00ca\2\2\u0284\u0286\5> \2\u0285")
        buf.write(u"\u0283\3\2\2\2\u0285\u0284\3\2\2\2\u0286=\3\2\2\2\u0287")
        buf.write(u"\u0288\t\2\2\2\u0288?\3\2\2\2\u0289\u028c\5t;\2\u028a")
        buf.write(u"\u028c\5B\"\2\u028b\u0289\3\2\2\2\u028b\u028a\3\2\2\2")
        buf.write(u"\u028cA\3\2\2\2\u028d\u0291\7\u00cb\2\2\u028e\u0291\5")
        buf.write(u"D#\2\u028f\u0291\5L\'\2\u0290\u028d\3\2\2\2\u0290\u028e")
        buf.write(u"\3\2\2\2\u0290\u028f\3\2\2\2\u0291C\3\2\2\2\u0292\u0296")
        buf.write(u"\5H%\2\u0293\u0296\5F$\2\u0294\u0296\5J&\2\u0295\u0292")
        buf.write(u"\3\2\2\2\u0295\u0293\3\2\2\2\u0295\u0294\3\2\2\2\u0296")
        buf.write(u"E\3\2\2\2\u0297\u0298\7\u00a0\2\2\u0298\u0299\7\u00cb")
        buf.write(u"\2\2\u0299G\3\2\2\2\u029a\u029b\7\u00a2\2\2\u029b\u029c")
        buf.write(u"\7\u00cb\2\2\u029cI\3\2\2\2\u029d\u029e\7\u009f\2\2\u029e")
        buf.write(u"\u029f\7\u00cb\2\2\u029fK\3\2\2\2\u02a0\u02a1\t\3\2\2")
        buf.write(u"\u02a1M\3\2\2\2\u02a2\u02a3\5P)\2\u02a3O\3\2\2\2\u02a4")
        buf.write(u"\u02ae\5T+\2\u02a5\u02ae\5X-\2\u02a6\u02ae\5Z.\2\u02a7")
        buf.write(u"\u02ae\5\\/\2\u02a8\u02ae\5d\63\2\u02a9\u02ae\5f\64\2")
        buf.write(u"\u02aa\u02ae\5h\65\2\u02ab\u02ae\5j\66\2\u02ac\u02ae")
        buf.write(u"\5R*\2\u02ad\u02a4\3\2\2\2\u02ad\u02a5\3\2\2\2\u02ad")
        buf.write(u"\u02a6\3\2\2\2\u02ad\u02a7\3\2\2\2\u02ad\u02a8\3\2\2")
        buf.write(u"\2\u02ad\u02a9\3\2\2\2\u02ad\u02aa\3\2\2\2\u02ad\u02ab")
        buf.write(u"\3\2\2\2\u02ad\u02ac\3\2\2\2\u02aeQ\3\2\2\2\u02af\u02b0")
        buf.write(u"\7\u00a9\2\2\u02b0S\3\2\2\2\u02b1\u02b3\7<\2\2\u02b2")
        buf.write(u"\u02b4\5V,\2\u02b3\u02b2\3\2\2\2\u02b3\u02b4\3\2\2\2")
        buf.write(u"\u02b4\u02c9\3\2\2\2\u02b5\u02b7\7\u009b\2\2\u02b6\u02b8")
        buf.write(u"\5V,\2\u02b7\u02b6\3\2\2\2\u02b7\u02b8\3\2\2\2\u02b8")
        buf.write(u"\u02c9\3\2\2\2\u02b9\u02ba\7<\2\2\u02ba\u02bc\7\u0083")
        buf.write(u"\2\2\u02bb\u02bd\5V,\2\u02bc\u02bb\3\2\2\2\u02bc\u02bd")
        buf.write(u"\3\2\2\2\u02bd\u02c9\3\2\2\2\u02be\u02bf\7\u009b\2\2")
        buf.write(u"\u02bf\u02c1\7\u0083\2\2\u02c0\u02c2\5V,\2\u02c1\u02c0")
        buf.write(u"\3\2\2\2\u02c1\u02c2\3\2\2\2\u02c2\u02c9\3\2\2\2\u02c3")
        buf.write(u"\u02c5\7\u009c\2\2\u02c4\u02c6\5V,\2\u02c5\u02c4\3\2")
        buf.write(u"\2\2\u02c5\u02c6\3\2\2\2\u02c6\u02c9\3\2\2\2\u02c7\u02c9")
        buf.write(u"\7\u00a4\2\2\u02c8\u02b1\3\2\2\2\u02c8\u02b5\3\2\2\2")
        buf.write(u"\u02c8\u02b9\3\2\2\2\u02c8\u02be\3\2\2\2\u02c8\u02c3")
        buf.write(u"\3\2\2\2\u02c8\u02c7\3\2\2\2\u02c9U\3\2\2\2\u02ca\u02cb")
        buf.write(u"\7\u00ba\2\2\u02cb\u02cc\7\u00c6\2\2\u02cc\u02cd\7\u00bb")
        buf.write(u"\2\2\u02cdW\3\2\2\2\u02ce\u02cf\7e\2\2\u02cf\u02d1\7")
        buf.write(u"<\2\2\u02d0\u02d2\5V,\2\u02d1\u02d0\3\2\2\2\u02d1\u02d2")
        buf.write(u"\3\2\2\2\u02d2\u02f2\3\2\2\2\u02d3\u02d4\7e\2\2\u02d4")
        buf.write(u"\u02d6\7\u009b\2\2\u02d5\u02d7\5V,\2\u02d6\u02d5\3\2")
        buf.write(u"\2\2\u02d6\u02d7\3\2\2\2\u02d7\u02f2\3\2\2\2\u02d8\u02da")
        buf.write(u"\7\u009d\2\2\u02d9\u02db\5V,\2\u02da\u02d9\3\2\2\2\u02da")
        buf.write(u"\u02db\3\2\2\2\u02db\u02f2\3\2\2\2\u02dc\u02dd\7e\2\2")
        buf.write(u"\u02dd\u02de\7<\2\2\u02de\u02e0\7\u0083\2\2\u02df\u02e1")
        buf.write(u"\5V,\2\u02e0\u02df\3\2\2\2\u02e0\u02e1\3\2\2\2\u02e1")
        buf.write(u"\u02f2\3\2\2\2\u02e2\u02e3\7e\2\2\u02e3\u02e4\7\u009b")
        buf.write(u"\2\2\u02e4\u02e6\7\u0083\2\2\u02e5\u02e7\5V,\2\u02e6")
        buf.write(u"\u02e5\3\2\2\2\u02e6\u02e7\3\2\2\2\u02e7\u02f2\3\2\2")
        buf.write(u"\2\u02e8\u02e9\7\u009d\2\2\u02e9\u02eb\7\u0083\2\2\u02ea")
        buf.write(u"\u02ec\5V,\2\u02eb\u02ea\3\2\2\2\u02eb\u02ec\3\2\2\2")
        buf.write(u"\u02ec\u02f2\3\2\2\2\u02ed\u02ef\7\u009e\2\2\u02ee\u02f0")
        buf.write(u"\5V,\2\u02ef\u02ee\3\2\2\2\u02ef\u02f0\3\2\2\2\u02f0")
        buf.write(u"\u02f2\3\2\2\2\u02f1\u02ce\3\2\2\2\u02f1\u02d3\3\2\2")
        buf.write(u"\2\u02f1\u02d8\3\2\2\2\u02f1\u02dc\3\2\2\2\u02f1\u02e2")
        buf.write(u"\3\2\2\2\u02f1\u02e8\3\2\2\2\u02f1\u02ed\3\2\2\2\u02f2")
        buf.write(u"Y\3\2\2\2\u02f3\u02f5\7\u00a7\2\2\u02f4\u02f6\5V,\2\u02f5")
        buf.write(u"\u02f4\3\2\2\2\u02f5\u02f6\3\2\2\2\u02f6\u02fc\3\2\2")
        buf.write(u"\2\u02f7\u02f9\7\u00a8\2\2\u02f8\u02fa\5V,\2\u02f9\u02f8")
        buf.write(u"\3\2\2\2\u02f9\u02fa\3\2\2\2\u02fa\u02fc\3\2\2\2\u02fb")
        buf.write(u"\u02f3\3\2\2\2\u02fb\u02f7\3\2\2\2\u02fc[\3\2\2\2\u02fd")
        buf.write(u"\u0300\5^\60\2\u02fe\u0300\5`\61\2\u02ff\u02fd\3\2\2")
        buf.write(u"\2\u02ff\u02fe\3\2\2\2\u0300]\3\2\2\2\u0301\u0303\7\u0099")
        buf.write(u"\2\2\u0302\u0304\5b\62\2\u0303\u0302\3\2\2\2\u0303\u0304")
        buf.write(u"\3\2\2\2\u0304\u0317\3\2\2\2\u0305\u0307\7\u009a\2\2")
        buf.write(u"\u0306\u0308\5b\62\2\u0307\u0306\3\2\2\2\u0307\u0308")
        buf.write(u"\3\2\2\2\u0308\u0317\3\2\2\2\u0309\u030b\7C\2\2\u030a")
        buf.write(u"\u030c\5b\62\2\u030b\u030a\3\2\2\2\u030b\u030c\3\2\2")
        buf.write(u"\2\u030c\u0317\3\2\2\2\u030d\u0317\7\u008b\2\2\u030e")
        buf.write(u"\u0317\7\u008f\2\2\u030f\u0317\7\u008c\2\2\u0310\u0317")
        buf.write(u"\7\u0090\2\2\u0311\u0317\7\u008d\2\2\u0312\u0317\7\u0091")
        buf.write(u"\2\2\u0313\u0317\7\u0092\2\2\u0314\u0317\7\u008e\2\2")
        buf.write(u"\u0315\u0317\7\u0093\2\2\u0316\u0301\3\2\2\2\u0316\u0305")
        buf.write(u"\3\2\2\2\u0316\u0309\3\2\2\2\u0316\u030d\3\2\2\2\u0316")
        buf.write(u"\u030e\3\2\2\2\u0316\u030f\3\2\2\2\u0316\u0310\3\2\2")
        buf.write(u"\2\u0316\u0311\3\2\2\2\u0316\u0312\3\2\2\2\u0316\u0313")
        buf.write(u"\3\2\2\2\u0316\u0314\3\2\2\2\u0316\u0315\3\2\2\2\u0317")
        buf.write(u"_\3\2\2\2\u0318\u031a\7\u0097\2\2\u0319\u031b\5b\62\2")
        buf.write(u"\u031a\u0319\3\2\2\2\u031a\u031b\3\2\2\2\u031b\u0323")
        buf.write(u"\3\2\2\2\u031c\u0323\7\u0094\2\2\u031d\u0323\7\u0096")
        buf.write(u"\2\2\u031e\u0323\7\u0095\2\2\u031f\u0323\7\u0098\2\2")
        buf.write(u"\u0320\u0321\7\u0098\2\2\u0321\u0323\7j\2\2\u0322\u0318")
        buf.write(u"\3\2\2\2\u0322\u031c\3\2\2\2\u0322\u031d\3\2\2\2\u0322")
        buf.write(u"\u031e\3\2\2\2\u0322\u031f\3\2\2\2\u0322\u0320\3\2\2")
        buf.write(u"\2\u0323a\3\2\2\2\u0324\u0325\7\u00ba\2\2\u0325\u0326")
        buf.write(u"\7\u00c6\2\2\u0326\u032d\7\u00bb\2\2\u0327\u0328\7\u00ba")
        buf.write(u"\2\2\u0328\u0329\7\u00c6\2\2\u0329\u032a\7\u00b3\2\2")
        buf.write(u"\u032a\u032b\7\u00c6\2\2\u032b\u032d\7\u00bb\2\2\u032c")
        buf.write(u"\u0324\3\2\2\2\u032c\u0327\3\2\2\2\u032dc\3\2\2\2\u032e")
        buf.write(u"\u032f\t\4\2\2\u032fe\3\2\2\2\u0330\u033e\7\u009f\2\2")
        buf.write(u"\u0331\u033e\7\u00a0\2\2\u0332\u0333\7\u00a0\2\2\u0333")
        buf.write(u"\u0334\7\67\2\2\u0334\u0335\7\u00a0\2\2\u0335\u033e\7")
        buf.write(u"\u0086\2\2\u0336\u033e\7\u00a1\2\2\u0337\u033e\7\u00a2")
        buf.write(u"\2\2\u0338\u0339\7\u00a2\2\2\u0339\u033a\7\67\2\2\u033a")
        buf.write(u"\u033b\7\u00a0\2\2\u033b\u033e\7\u0086\2\2\u033c\u033e")
        buf.write(u"\7\u00a3\2\2\u033d\u0330\3\2\2\2\u033d\u0331\3\2\2\2")
        buf.write(u"\u033d\u0332\3\2\2\2\u033d\u0336\3\2\2\2\u033d\u0337")
        buf.write(u"\3\2\2\2\u033d\u0338\3\2\2\2\u033d\u033c\3\2\2\2\u033e")
        buf.write(u"g\3\2\2\2\u033f\u0341\7\u0089\2\2\u0340\u0342\5V,\2\u0341")
        buf.write(u"\u0340\3\2\2\2\u0341\u0342\3\2\2\2\u0342\u034d\3\2\2")
        buf.write(u"\2\u0343\u0345\7\u008a\2\2\u0344\u0346\5V,\2\u0345\u0344")
        buf.write(u"\3\2\2\2\u0345\u0346\3\2\2\2\u0346\u034d\3\2\2\2\u0347")
        buf.write(u"\u0348\7\u0089\2\2\u0348\u034a\7\u0083\2\2\u0349\u034b")
        buf.write(u"\5V,\2\u034a\u0349\3\2\2\2\u034a\u034b\3\2\2\2\u034b")
        buf.write(u"\u034d\3\2\2\2\u034c\u033f\3\2\2\2\u034c\u0343\3\2\2")
        buf.write(u"\2\u034c\u0347\3\2\2\2\u034di\3\2\2\2\u034e\u0350\7\u00a5")
        buf.write(u"\2\2\u034f\u0351\5V,\2\u0350\u034f\3\2\2\2\u0350\u0351")
        buf.write(u"\3\2\2\2\u0351\u035c\3\2\2\2\u0352\u0353\7\u00a5\2\2")
        buf.write(u"\u0353\u0355\7\u0083\2\2\u0354\u0356\5V,\2\u0355\u0354")
        buf.write(u"\3\2\2\2\u0355\u0356\3\2\2\2\u0356\u035c\3\2\2\2\u0357")
        buf.write(u"\u0359\7\u00a6\2\2\u0358\u035a\5V,\2\u0359\u0358\3\2")
        buf.write(u"\2\2\u0359\u035a\3\2\2\2\u035a\u035c\3\2\2\2\u035b\u034e")
        buf.write(u"\3\2\2\2\u035b\u0352\3\2\2\2\u035b\u0357\3\2\2\2\u035c")
        buf.write(u"k\3\2\2\2\u035d\u0360\5n8\2\u035e\u0360\5p9\2\u035f\u035d")
        buf.write(u"\3\2\2\2\u035f\u035e\3\2\2\2\u0360m\3\2\2\2\u0361\u0362")
        buf.write(u"\7\u00ba\2\2\u0362\u0363\5\u009cO\2\u0363\u0364\7\u00bb")
        buf.write(u"\2\2\u0364o\3\2\2\2\u0365\u036d\5r:\2\u0366\u036d\5\u0144")
        buf.write(u"\u00a3\2\u0367\u036d\5x=\2\u0368\u036d\5\u014a\u00a6")
        buf.write(u"\2\u0369\u036d\5\u0084C\2\u036a\u036d\5\u0096L\2\u036b")
        buf.write(u"\u036d\5\u017e\u00c0\2\u036c\u0365\3\2\2\2\u036c\u0366")
        buf.write(u"\3\2\2\2\u036c\u0367\3\2\2\2\u036c\u0368\3\2\2\2\u036c")
        buf.write(u"\u0369\3\2\2\2\u036c\u036a\3\2\2\2\u036c\u036b\3\2\2")
        buf.write(u"\2\u036dq\3\2\2\2\u036e\u036f\5@!\2\u036fs\3\2\2\2\u0370")
        buf.write(u"\u0371\t\5\2\2\u0371u\3\2\2\2\u0372\u0374\5\u00aaV\2")
        buf.write(u"\u0373\u0372\3\2\2\2\u0373\u0374\3\2\2\2\u0374\u0375")
        buf.write(u"\3\2\2\2\u0375\u0376\5t;\2\u0376w\3\2\2\2\u0377\u0378")
        buf.write(u"\5z>\2\u0378y\3\2\2\2\u0379\u037a\7@\2\2\u037a\u037b")
        buf.write(u"\7\u00ba\2\2\u037b\u037c\7\u00be\2\2\u037c\u0382\7\u00bb")
        buf.write(u"\2\2\u037d\u037f\5|?\2\u037e\u0380\5\u0080A\2\u037f\u037e")
        buf.write(u"\3\2\2\2\u037f\u0380\3\2\2\2\u0380\u0382\3\2\2\2\u0381")
        buf.write(u"\u0379\3\2\2\2\u0381\u037d\3\2\2\2\u0382{\3\2\2\2\u0383")
        buf.write(u"\u0384\5~@\2\u0384\u0386\7\u00ba\2\2\u0385\u0387\5\u0142")
        buf.write(u"\u00a2\2\u0386\u0385\3\2\2\2\u0386\u0387\3\2\2\2\u0387")
        buf.write(u"\u0388\3\2\2\2\u0388\u0389\5\u009cO\2\u0389\u038a\7\u00bb")
        buf.write(u"\2\2\u038a}\3\2\2\2\u038b\u038c\t\6\2\2\u038c\177\3\2")
        buf.write(u"\2\2\u038d\u038e\7M\2\2\u038e\u038f\7\u00ba\2\2\u038f")
        buf.write(u"\u0390\7\66\2\2\u0390\u0391\5\u010c\u0087\2\u0391\u0392")
        buf.write(u"\7\u00bb\2\2\u0392\u0081\3\2\2\2\u0393\u0394\7Q\2\2\u0394")
        buf.write(u"\u0395\7\u00ba\2\2\u0395\u0396\5\u0148\u00a5\2\u0396")
        buf.write(u"\u0397\7\u00bb\2\2\u0397\u0083\3\2\2\2\u0398\u0399\5")
        buf.write(u"\u0088E\2\u0399\u0085\3\2\2\2\u039a\u039b\7f\2\2\u039b")
        buf.write(u"\u039c\7\u00ba\2\2\u039c\u039d\5\u00a0Q\2\u039d\u039e")
        buf.write(u"\7\u00b3\2\2\u039e\u039f\5\u00c6d\2\u039f\u03a0\7\u00bb")
        buf.write(u"\2\2\u03a0\u03ad\3\2\2\2\u03a1\u03a2\7>\2\2\u03a2\u03a3")
        buf.write(u"\7\u00ba\2\2\u03a3\u03a6\5\u00a0Q\2\u03a4\u03a5\7\u00b3")
        buf.write(u"\2\2\u03a5\u03a7\5\u00c6d\2\u03a6\u03a4\3\2\2\2\u03a7")
        buf.write(u"\u03a8\3\2\2\2\u03a8\u03a6\3\2\2\2\u03a8\u03a9\3\2\2")
        buf.write(u"\2\u03a9\u03aa\3\2\2\2\u03aa\u03ab\7\u00bb\2\2\u03ab")
        buf.write(u"\u03ad\3\2\2\2\u03ac\u039a\3\2\2\2\u03ac\u03a1\3\2\2")
        buf.write(u"\2\u03ad\u0087\3\2\2\2\u03ae\u03b1\5\u008aF\2\u03af\u03b1")
        buf.write(u"\5\u008cG\2\u03b0\u03ae\3\2\2\2\u03b0\u03af\3\2\2\2\u03b1")
        buf.write(u"\u0089\3\2\2\2\u03b2\u03b3\7\n\2\2\u03b3\u03b5\5\u00c6")
        buf.write(u"d\2\u03b4\u03b6\5\u008eH\2\u03b5\u03b4\3\2\2\2\u03b6")
        buf.write(u"\u03b7\3\2\2\2\u03b7\u03b5\3\2\2\2\u03b7\u03b8\3\2\2")
        buf.write(u"\2\u03b8\u03ba\3\2\2\2\u03b9\u03bb\5\u0092J\2\u03ba\u03b9")
        buf.write(u"\3\2\2\2\u03ba\u03bb\3\2\2\2\u03bb\u03bc\3\2\2\2\u03bc")
        buf.write(u"\u03bd\7\20\2\2\u03bd\u008b\3\2\2\2\u03be\u03c0\7\n\2")
        buf.write(u"\2\u03bf\u03c1\5\u0090I\2\u03c0\u03bf\3\2\2\2\u03c1\u03c2")
        buf.write(u"\3\2\2\2\u03c2\u03c0\3\2\2\2\u03c2\u03c3\3\2\2\2\u03c3")
        buf.write(u"\u03c5\3\2\2\2\u03c4\u03c6\5\u0092J\2\u03c5\u03c4\3\2")
        buf.write(u"\2\2\u03c5\u03c6\3\2\2\2\u03c6\u03c7\3\2\2\2\u03c7\u03c8")
        buf.write(u"\7\20\2\2\u03c8\u008d\3\2\2\2\u03c9\u03ca\7\65\2\2\u03ca")
        buf.write(u"\u03cb\5\u010c\u0087\2\u03cb\u03cc\7/\2\2\u03cc\u03cd")
        buf.write(u"\5\u0094K\2\u03cd\u008f\3\2\2\2\u03ce\u03cf\7\65\2\2")
        buf.write(u"\u03cf\u03d0\5\u010c\u0087\2\u03d0\u03d1\7/\2\2\u03d1")
        buf.write(u"\u03d2\5\u0094K\2\u03d2\u0091\3\2\2\2\u03d3\u03d4\7\21")
        buf.write(u"\2\2\u03d4\u03d5\5\u0094K\2\u03d5\u0093\3\2\2\2\u03d6")
        buf.write(u"\u03d9\5\u009cO\2\u03d7\u03d9\7%\2\2\u03d8\u03d6\3\2")
        buf.write(u"\2\2\u03d8\u03d7\3\2\2\2\u03d9\u0095\3\2\2\2\u03da\u03db")
        buf.write(u"\7\13\2\2\u03db\u03dc\7\u00ba\2\2\u03dc\u03dd\5\u0098")
        buf.write(u"M\2\u03dd\u03de\7\3\2\2\u03de\u03df\5\u009aN\2\u03df")
        buf.write(u"\u03e0\7\u00bb\2\2\u03e0\u0097\3\2\2\2\u03e1\u03e2\5")
        buf.write(u"\u009cO\2\u03e2\u0099\3\2\2\2\u03e3\u03e4\5N(\2\u03e4")
        buf.write(u"\u009b\3\2\2\2\u03e5\u03e9\5\u009eP\2\u03e6\u03e9\5\u00da")
        buf.write(u"n\2\u03e7\u03e9\5\u00c6d\2\u03e8\u03e5\3\2\2\2\u03e8")
        buf.write(u"\u03e6\3\2\2\2\u03e8\u03e7\3\2\2\2\u03e9\u009d\3\2\2")
        buf.write(u"\2\u03ea\u03ee\5\u00a0Q\2\u03eb\u03ee\5\u00b6\\\2\u03ec")
        buf.write(u"\u03ee\7%\2\2\u03ed\u03ea\3\2\2\2\u03ed\u03eb\3\2\2\2")
        buf.write(u"\u03ed\u03ec\3\2\2\2\u03ee\u009f\3\2\2\2\u03ef\u03f4")
        buf.write(u"\5\u00a2R\2\u03f0\u03f1\t\7\2\2\u03f1\u03f3\5\u00a2R")
        buf.write(u"\2\u03f2\u03f0\3\2\2\2\u03f3\u03f6\3\2\2\2\u03f4\u03f2")
        buf.write(u"\3\2\2\2\u03f4\u03f5\3\2\2\2\u03f5\u00a1\3\2\2\2\u03f6")
        buf.write(u"\u03f4\3\2\2\2\u03f7\u03fc\5\u00a4S\2\u03f8\u03f9\t\b")
        buf.write(u"\2\2\u03f9\u03fb\5\u00a4S\2\u03fa\u03f8\3\2\2\2\u03fb")
        buf.write(u"\u03fe\3\2\2\2\u03fc\u03fa\3\2\2\2\u03fc\u03fd\3\2\2")
        buf.write(u"\2\u03fd\u00a3\3\2\2\2\u03fe\u03fc\3\2\2\2\u03ff\u0401")
        buf.write(u"\5\u00aaV\2\u0400\u03ff\3\2\2\2\u0400\u0401\3\2\2\2\u0401")
        buf.write(u"\u0402\3\2\2\2\u0402\u0403\5\u00a8U\2\u0403\u00a5\3\2")
        buf.write(u"\2\2\u0404\u0405\7\u00ba\2\2\u0405\u040a\5\u00a0Q\2\u0406")
        buf.write(u"\u0407\7\u00b3\2\2\u0407\u0409\5\u00a0Q\2\u0408\u0406")
        buf.write(u"\3\2\2\2\u0409\u040c\3\2\2\2\u040a\u0408\3\2\2\2\u040a")
        buf.write(u"\u040b\3\2\2\2\u040b\u040d\3\2\2\2\u040c\u040a\3\2\2")
        buf.write(u"\2\u040d\u040e\7\u00bb\2\2\u040e\u00a7\3\2\2\2\u040f")
        buf.write(u"\u0414\5l\67\2\u0410\u0411\7\u00ae\2\2\u0411\u0413\5")
        buf.write(u"\u009aN\2\u0412\u0410\3\2\2\2\u0413\u0416\3\2\2\2\u0414")
        buf.write(u"\u0412\3\2\2\2\u0414\u0415\3\2\2\2\u0415\u0419\3\2\2")
        buf.write(u"\2\u0416\u0414\3\2\2\2\u0417\u0419\5\u00acW\2\u0418\u040f")
        buf.write(u"\3\2\2\2\u0418\u0417\3\2\2\2\u0419\u00a9\3\2\2\2\u041a")
        buf.write(u"\u041b\t\7\2\2\u041b\u00ab\3\2\2\2\u041c\u041d\5\u00ae")
        buf.write(u"X\2\u041d\u00ad\3\2\2\2\u041e\u041f\7L\2\2\u041f\u0420")
        buf.write(u"\7\u00ba\2\2\u0420\u0421\5\u00b0Y\2\u0421\u0422\7\25")
        buf.write(u"\2\2\u0422\u0423\5\u00b4[\2\u0423\u0424\7\u00bb\2\2\u0424")
        buf.write(u"\u00af\3\2\2\2\u0425\u0429\5\u0178\u00bd\2\u0426\u0429")
        buf.write(u"\5\u00b2Z\2\u0427\u0429\5\u017c\u00bf\2\u0428\u0425\3")
        buf.write(u"\2\2\2\u0428\u0426\3\2\2\2\u0428\u0427\3\2\2\2\u0429")
        buf.write(u"\u00b1\3\2\2\2\u042a\u042b\t\t\2\2\u042b\u00b3\3\2\2")
        buf.write(u"\2\u042c\u042f\5\u0144\u00a3\2\u042d\u042f\5D#\2\u042e")
        buf.write(u"\u042c\3\2\2\2\u042e\u042d\3\2\2\2\u042f\u00b5\3\2\2")
        buf.write(u"\2\u0430\u0431\5\u00b8]\2\u0431\u00b7\3\2\2\2\u0432\u0437")
        buf.write(u"\5\u00ba^\2\u0433\u0434\7\u00b4\2\2\u0434\u0436\5\u00ba")
        buf.write(u"^\2\u0435\u0433\3\2\2\2\u0436\u0439\3\2\2\2\u0437\u0435")
        buf.write(u"\3\2\2\2\u0437\u0438\3\2\2\2\u0438\u00b9\3\2\2\2\u0439")
        buf.write(u"\u0437\3\2\2\2\u043a\u043b\5\u00bc_\2\u043b\u00bb\3\2")
        buf.write(u"\2\2\u043c\u043f\5l\67\2\u043d\u043f\5\u00be`\2\u043e")
        buf.write(u"\u043c\3\2\2\2\u043e\u043d\3\2\2\2\u043f\u00bd\3\2\2")
        buf.write(u"\2\u0440\u0441\5\u00c0a\2\u0441\u00bf\3\2\2\2\u0442\u0443")
        buf.write(u"\7}\2\2\u0443\u0444\7\u00ba\2\2\u0444\u0445\5\u00c2b")
        buf.write(u"\2\u0445\u0446\7\u00bb\2\2\u0446\u00c1\3\2\2\2\u0447")
        buf.write(u"\u0449\5\u00c4c\2\u0448\u0447\3\2\2\2\u0448\u0449\3\2")
        buf.write(u"\2\2\u0449\u044b\3\2\2\2\u044a\u044c\5\u00b8]\2\u044b")
        buf.write(u"\u044a\3\2\2\2\u044b\u044c\3\2\2\2\u044c\u044d\3\2\2")
        buf.write(u"\2\u044d\u044f\7\25\2\2\u044e\u0448\3\2\2\2\u044e\u044f")
        buf.write(u"\3\2\2\2\u044f\u0450\3\2\2\2\u0450\u0456\5\u00b8]\2\u0451")
        buf.write(u"\u0452\5\u00b8]\2\u0452\u0453\7\u00b3\2\2\u0453\u0454")
        buf.write(u"\5\u00b8]\2\u0454\u0456\3\2\2\2\u0455\u044e\3\2\2\2\u0455")
        buf.write(u"\u0451\3\2\2\2\u0456\u00c3\3\2\2\2\u0457\u0458\t\n\2")
        buf.write(u"\2\u0458\u00c5\3\2\2\2\u0459\u045a\5\u00c8e\2\u045a\u00c7")
        buf.write(u"\3\2\2\2\u045b\u0460\5\u00caf\2\u045c\u045d\7(\2\2\u045d")
        buf.write(u"\u045f\5\u00c8e\2\u045e\u045c\3\2\2\2\u045f\u0462\3\2")
        buf.write(u"\2\2\u0460\u045e\3\2\2\2\u0460\u0461\3\2\2\2\u0461\u00c9")
        buf.write(u"\3\2\2\2\u0462\u0460\3\2\2\2\u0463\u0468\5\u00ccg\2\u0464")
        buf.write(u"\u0465\7\5\2\2\u0465\u0467\5\u00caf\2\u0466\u0464\3\2")
        buf.write(u"\2\2\u0467\u046a\3\2\2\2\u0468\u0466\3\2\2\2\u0468\u0469")
        buf.write(u"\3\2\2\2\u0469\u00cb\3\2\2\2\u046a\u0468\3\2\2\2\u046b")
        buf.write(u"\u046f\5\u00ceh\2\u046c\u046d\7$\2\2\u046d\u046f\5\u00ce")
        buf.write(u"h\2\u046e\u046b\3\2\2\2\u046e\u046c\3\2\2\2\u046f\u00cd")
        buf.write(u"\3\2\2\2\u0470\u0472\5\u00d4k\2\u0471\u0473\5\u00d0i")
        buf.write(u"\2\u0472\u0471\3\2\2\2\u0472\u0473\3\2\2\2\u0473\u00cf")
        buf.write(u"\3\2\2\2\u0474\u0476\7\35\2\2\u0475\u0477\7$\2\2\u0476")
        buf.write(u"\u0475\3\2\2\2\u0476\u0477\3\2\2\2\u0477\u0478\3\2\2")
        buf.write(u"\2\u0478\u0479\5\u00d2j\2\u0479\u00d1\3\2\2\2\u047a\u047b")
        buf.write(u"\t\3\2\2\u047b\u00d3\3\2\2\2\u047c\u047f\5\u0152\u00aa")
        buf.write(u"\2\u047d\u047f\5\u00d6l\2\u047e\u047c\3\2\2\2\u047e\u047d")
        buf.write(u"\3\2\2\2\u047f\u00d5\3\2\2\2\u0480\u0483\5\u00d8m\2\u0481")
        buf.write(u"\u0483\5p9\2\u0482\u0480\3\2\2\2\u0482\u0481\3\2\2\2")
        buf.write(u"\u0483\u00d7\3\2\2\2\u0484\u0485\7\u00ba\2\2\u0485\u0486")
        buf.write(u"\5\u00c6d\2\u0486\u0487\7\u00bb\2\2\u0487\u00d9\3\2\2")
        buf.write(u"\2\u0488\u048b\5\u00dco\2\u0489\u048b\5\u00dep\2\u048a")
        buf.write(u"\u0488\3\2\2\2\u048a\u0489\3\2\2\2\u048b\u00db\3\2\2")
        buf.write(u"\2\u048c\u048d\5p9\2\u048d\u00dd\3\2\2\2\u048e\u048f")
        buf.write(u"\7%\2\2\u048f\u00df\3\2\2\2\u0490\u0493\5\u00dco\2\u0491")
        buf.write(u"\u0493\5\u00e2r\2\u0492\u0490\3\2\2\2\u0492\u0491\3\2")
        buf.write(u"\2\2\u0493\u00e1\3\2\2\2\u0494\u0497\5\u009eP\2\u0495")
        buf.write(u"\u0497\5\u00d6l\2\u0496\u0494\3\2\2\2\u0496\u0495\3\2")
        buf.write(u"\2\2\u0497\u00e3\3\2\2\2\u0498\u049a\5\u00e6t\2\u0499")
        buf.write(u"\u049b\5\u010a\u0086\2\u049a\u0499\3\2\2\2\u049a\u049b")
        buf.write(u"\3\2\2\2\u049b\u049d\3\2\2\2\u049c\u049e\5\u010e\u0088")
        buf.write(u"\2\u049d\u049c\3\2\2\2\u049d\u049e\3\2\2\2\u049e\u04a0")
        buf.write(u"\3\2\2\2\u049f\u04a1\5\u011e\u0090\2\u04a0\u049f\3\2")
        buf.write(u"\2\2\u04a0\u04a1\3\2\2\2\u04a1\u04a3\3\2\2\2\u04a2\u04a4")
        buf.write(u"\5\u0186\u00c4\2\u04a3\u04a2\3\2\2\2\u04a3\u04a4\3\2")
        buf.write(u"\2\2\u04a4\u04a6\3\2\2\2\u04a5\u04a7\5\u018e\u00c8\2")
        buf.write(u"\u04a6\u04a5\3\2\2\2\u04a6\u04a7\3\2\2\2\u04a7\u00e5")
        buf.write(u"\3\2\2\2\u04a8\u04a9\7\25\2\2\u04a9\u04aa\5\u00e8u\2")
        buf.write(u"\u04aa\u00e7\3\2\2\2\u04ab\u04b0\5\u00eav\2\u04ac\u04ad")
        buf.write(u"\7\u00b3\2\2\u04ad\u04af\5\u00eav\2\u04ae\u04ac\3\2\2")
        buf.write(u"\2\u04af\u04b2\3\2\2\2\u04b0\u04ae\3\2\2\2\u04b0\u04b1")
        buf.write(u"\3\2\2\2\u04b1\u00e9\3\2\2\2\u04b2\u04b0\3\2\2\2\u04b3")
        buf.write(u"\u04b6\5\u00ecw\2\u04b4\u04b6\5\u0104\u0083\2\u04b5\u04b3")
        buf.write(u"\3\2\2\2\u04b5\u04b4\3\2\2\2\u04b6\u00eb\3\2\2\2\u04b7")
        buf.write(u"\u04b9\5\u0104\u0083\2\u04b8\u04ba\5\u00eex\2\u04b9\u04b8")
        buf.write(u"\3\2\2\2\u04ba\u04bb\3\2\2\2\u04bb\u04b9\3\2\2\2\u04bb")
        buf.write(u"\u04bc\3\2\2\2\u04bc\u00ed\3\2\2\2\u04bd\u04be\7\r\2")
        buf.write(u"\2\u04be\u04bf\7\36\2\2\u04bf\u04d1\5\u0104\u0083\2\u04c0")
        buf.write(u"\u04c2\5\u00f8}\2\u04c1\u04c0\3\2\2\2\u04c1\u04c2\3\2")
        buf.write(u"\2\2\u04c2\u04c3\3\2\2\2\u04c3\u04c4\7\36\2\2\u04c4\u04c5")
        buf.write(u"\5\u0104\u0083\2\u04c5\u04c6\5\u00fe\u0080\2\u04c6\u04d1")
        buf.write(u"\3\2\2\2\u04c7\u04c9\7#\2\2\u04c8\u04ca\5\u00f8}\2\u04c9")
        buf.write(u"\u04c8\3\2\2\2\u04c9\u04ca\3\2\2\2\u04ca\u04cb\3\2\2")
        buf.write(u"\2\u04cb\u04cc\7\36\2\2\u04cc\u04d1\5\u0104\u0083\2\u04cd")
        buf.write(u"\u04ce\7\62\2\2\u04ce\u04cf\7\36\2\2\u04cf\u04d1\5\u0104")
        buf.write(u"\u0083\2\u04d0\u04bd\3\2\2\2\u04d0\u04c1\3\2\2\2\u04d0")
        buf.write(u"\u04c7\3\2\2\2\u04d0\u04cd\3\2\2\2\u04d1\u00ef\3\2\2")
        buf.write(u"\2\u04d2\u04d3\7\r\2\2\u04d3\u04d4\7\36\2\2\u04d4\u04d5")
        buf.write(u"\5\u0104\u0083\2\u04d5\u00f1\3\2\2\2\u04d6\u04d8\5\u00f8")
        buf.write(u"}\2\u04d7\u04d6\3\2\2\2\u04d7\u04d8\3\2\2\2\u04d8\u04d9")
        buf.write(u"\3\2\2\2\u04d9\u04da\7\36\2\2\u04da\u04db\5\u0104\u0083")
        buf.write(u"\2\u04db\u04dc\5\u00fe\u0080\2\u04dc\u00f3\3\2\2\2\u04dd")
        buf.write(u"\u04df\7#\2\2\u04de\u04e0\5\u00f8}\2\u04df\u04de\3\2")
        buf.write(u"\2\2\u04df\u04e0\3\2\2\2\u04e0\u04e1\3\2\2\2\u04e1\u04e2")
        buf.write(u"\7\36\2\2\u04e2\u04e3\5\u0104\u0083\2\u04e3\u00f5\3\2")
        buf.write(u"\2\2\u04e4\u04e5\7\62\2\2\u04e5\u04e6\7\36\2\2\u04e6")
        buf.write(u"\u04e7\5\u0104\u0083\2\u04e7\u00f7\3\2\2\2\u04e8\u04eb")
        buf.write(u"\7\32\2\2\u04e9\u04eb\5\u00fa~\2\u04ea\u04e8\3\2\2\2")
        buf.write(u"\u04ea\u04e9\3\2\2\2\u04eb\u00f9\3\2\2\2\u04ec\u04ee")
        buf.write(u"\5\u00fc\177\2\u04ed\u04ef\7\'\2\2\u04ee\u04ed\3\2\2")
        buf.write(u"\2\u04ee\u04ef\3\2\2\2\u04ef\u00fb\3\2\2\2\u04f0\u04f1")
        buf.write(u"\t\13\2\2\u04f1\u00fd\3\2\2\2\u04f2\u04f5\5\u0100\u0081")
        buf.write(u"\2\u04f3\u04f5\5\u0102\u0082\2\u04f4\u04f2\3\2\2\2\u04f4")
        buf.write(u"\u04f3\3\2\2\2\u04f5\u00ff\3\2\2\2\u04f6\u04f7\7&\2\2")
        buf.write(u"\u04f7\u04f8\5\u010c\u0087\2\u04f8\u0101\3\2\2\2\u04f9")
        buf.write(u"\u04fa\7\64\2\2\u04fa\u04fb\7\u00ba\2\2\u04fb\u04fc\5")
        buf.write(u"\u0148\u00a5\2\u04fc\u04fd\7\u00bb\2\2\u04fd\u0103\3")
        buf.write(u"\2\2\2\u04fe\u0503\5\u0134\u009b\2\u04ff\u0501\7\3\2")
        buf.write(u"\2\u0500\u04ff\3\2\2\2\u0500\u0501\3\2\2\2\u0501\u0502")
        buf.write(u"\3\2\2\2\u0502\u0504\5<\37\2\u0503\u0500\3\2\2\2\u0503")
        buf.write(u"\u0504\3\2\2\2\u0504\u0509\3\2\2\2\u0505\u0506\7\u00ba")
        buf.write(u"\2\2\u0506\u0507\5\u0106\u0084\2\u0507\u0508\7\u00bb")
        buf.write(u"\2\2\u0508\u050a\3\2\2\2\u0509\u0505\3\2\2\2\u0509\u050a")
        buf.write(u"\3\2\2\2\u050a\u0517\3\2\2\2\u050b\u050d\5\u0108\u0085")
        buf.write(u"\2\u050c\u050e\7\3\2\2\u050d\u050c\3\2\2\2\u050d\u050e")
        buf.write(u"\3\2\2\2\u050e\u050f\3\2\2\2\u050f\u0514\5<\37\2\u0510")
        buf.write(u"\u0511\7\u00ba\2\2\u0511\u0512\5\u0106\u0084\2\u0512")
        buf.write(u"\u0513\7\u00bb\2\2\u0513\u0515\3\2\2\2\u0514\u0510\3")
        buf.write(u"\2\2\2\u0514\u0515\3\2\2\2\u0515\u0517\3\2\2\2\u0516")
        buf.write(u"\u04fe\3\2\2\2\u0516\u050b\3\2\2\2\u0517\u0105\3\2\2")
        buf.write(u"\2\u0518\u051d\5<\37\2\u0519\u051a\7\u00b3\2\2\u051a")
        buf.write(u"\u051c\5<\37\2\u051b\u0519\3\2\2\2\u051c\u051f\3\2\2")
        buf.write(u"\2\u051d\u051b\3\2\2\2\u051d\u051e\3\2\2\2\u051e\u0107")
        buf.write(u"\3\2\2\2\u051f\u051d\3\2\2\2\u0520\u0521\5\u014e\u00a8")
        buf.write(u"\2\u0521\u0109\3\2\2\2\u0522\u0523\7\66\2\2\u0523\u0524")
        buf.write(u"\5\u010c\u0087\2\u0524\u010b\3\2\2\2\u0525\u0526\5\u009c")
        buf.write(u"O\2\u0526\u010d\3\2\2\2\u0527\u0528\7\26\2\2\u0528\u0529")
        buf.write(u"\7:\2\2\u0529\u052a\5\u0110\u0089\2\u052a\u010f\3\2\2")
        buf.write(u"\2\u052b\u0530\5\u0112\u008a\2\u052c\u052d\7\u00b3\2")
        buf.write(u"\2\u052d\u052f\5\u0112\u008a\2\u052e\u052c\3\2\2\2\u052f")
        buf.write(u"\u0532\3\2\2\2\u0530\u052e\3\2\2\2\u0530\u0531\3\2\2")
        buf.write(u"\2\u0531\u0111\3\2\2\2\u0532\u0530\3\2\2\2\u0533\u0538")
        buf.write(u"\5\u0118\u008d\2\u0534\u0538\5\u011a\u008e\2\u0535\u0538")
        buf.write(u"\5\u011c\u008f\2\u0536\u0538\5\u0114\u008b\2\u0537\u0533")
        buf.write(u"\3\2\2\2\u0537\u0534\3\2\2\2\u0537\u0535\3\2\2\2\u0537")
        buf.write(u"\u0536\3\2\2\2\u0538\u0113\3\2\2\2\u0539\u053f\5\u00e0")
        buf.write(u"q\2\u053a\u053b\7\u00ba\2\2\u053b\u053c\5\u0120\u0091")
        buf.write(u"\2\u053c\u053d\7\u00bb\2\2\u053d\u053f\3\2\2\2\u053e")
        buf.write(u"\u0539\3\2\2\2\u053e\u053a\3\2\2\2\u053f\u0115\3\2\2")
        buf.write(u"\2\u0540\u0545\5\u0114\u008b\2\u0541\u0542\7\u00b3\2")
        buf.write(u"\2\u0542\u0544\5\u0114\u008b\2\u0543\u0541\3\2\2\2\u0544")
        buf.write(u"\u0547\3\2\2\2\u0545\u0543\3\2\2\2\u0545\u0546\3\2\2")
        buf.write(u"\2\u0546\u0117\3\2\2\2\u0547\u0545\3\2\2\2\u0548\u0549")
        buf.write(u"\7p\2\2\u0549\u054a\7\u00ba\2\2\u054a\u054b\5\u0116\u008c")
        buf.write(u"\2\u054b\u054c\7\u00bb\2\2\u054c\u0119\3\2\2\2\u054d")
        buf.write(u"\u054e\7A\2\2\u054e\u054f\7\u00ba\2\2\u054f\u0550\5\u0116")
        buf.write(u"\u008c\2\u0550\u0551\7\u00bb\2\2\u0551\u011b\3\2\2\2")
        buf.write(u"\u0552\u0553\7\u00ba\2\2\u0553\u0554\7\u00bb\2\2\u0554")
        buf.write(u"\u011d\3\2\2\2\u0555\u0556\7\27\2\2\u0556\u0557\5\u00c6")
        buf.write(u"d\2\u0557\u011f\3\2\2\2\u0558\u055d\5\u00e0q\2\u0559")
        buf.write(u"\u055a\7\u00b3\2\2\u055a\u055c\5\u00e0q\2\u055b\u0559")
        buf.write(u"\3\2\2\2\u055c\u055f\3\2\2\2\u055d\u055b\3\2\2\2\u055d")
        buf.write(u"\u055e\3\2\2\2\u055e\u0121\3\2\2\2\u055f\u055d\3\2\2")
        buf.write(u"\2\u0560\u0561\5\u0124\u0093\2\u0561\u0123\3\2\2\2\u0562")
        buf.write(u"\u0565\5\u0126\u0094\2\u0563\u0565\5\u00ecw\2\u0564\u0562")
        buf.write(u"\3\2\2\2\u0564\u0563\3\2\2\2\u0565\u0125\3\2\2\2\u0566")
        buf.write(u"\u056f\5\u012a\u0096\2\u0567\u0568\5\u00ecw\2\u0568\u056a")
        buf.write(u"\t\f\2\2\u0569\u056b\t\r\2\2\u056a\u0569\3\2\2\2\u056a")
        buf.write(u"\u056b\3\2\2\2\u056b\u056c\3\2\2\2\u056c\u056d\5\u0128")
        buf.write(u"\u0095\2\u056d\u056f\3\2\2\2\u056e\u0566\3\2\2\2\u056e")
        buf.write(u"\u0567\3\2\2\2\u056f\u0577\3\2\2\2\u0570\u0572\t\f\2")
        buf.write(u"\2\u0571\u0573\t\r\2\2\u0572\u0571\3\2\2\2\u0572\u0573")
        buf.write(u"\3\2\2\2\u0573\u0574\3\2\2\2\u0574\u0576\5\u0128\u0095")
        buf.write(u"\2\u0575\u0570\3\2\2\2\u0576\u0579\3\2\2\2\u0577\u0575")
        buf.write(u"\3\2\2\2\u0577\u0578\3\2\2\2\u0578\u0127\3\2\2\2\u0579")
        buf.write(u"\u0577\3\2\2\2\u057a\u057d\5\u012a\u0096\2\u057b\u057d")
        buf.write(u"\5\u00ecw\2\u057c\u057a\3\2\2\2\u057c\u057b\3\2\2\2\u057d")
        buf.write(u"\u0129\3\2\2\2\u057e\u0587\5\u012e\u0098\2\u057f\u0580")
        buf.write(u"\5\u00ecw\2\u0580\u0582\7\33\2\2\u0581\u0583\t\r\2\2")
        buf.write(u"\u0582\u0581\3\2\2\2\u0582\u0583\3\2\2\2\u0583\u0584")
        buf.write(u"\3\2\2\2\u0584\u0585\5\u012c\u0097\2\u0585\u0587\3\2")
        buf.write(u"\2\2\u0586\u057e\3\2\2\2\u0586\u057f\3\2\2\2\u0587\u058f")
        buf.write(u"\3\2\2\2\u0588\u058a\7\33\2\2\u0589\u058b\t\r\2\2\u058a")
        buf.write(u"\u0589\3\2\2\2\u058a\u058b\3\2\2\2\u058b\u058c\3\2\2")
        buf.write(u"\2\u058c\u058e\5\u012c\u0097\2\u058d\u0588\3\2\2\2\u058e")
        buf.write(u"\u0591\3\2\2\2\u058f\u058d\3\2\2\2\u058f\u0590\3\2\2")
        buf.write(u"\2\u0590\u012b\3\2\2\2\u0591\u058f\3\2\2\2\u0592\u0595")
        buf.write(u"\5\u012e\u0098\2\u0593\u0595\5\u00ecw\2\u0594\u0592\3")
        buf.write(u"\2\2\2\u0594\u0593\3\2\2\2\u0595\u012d\3\2\2\2\u0596")
        buf.write(u"\u059c\5\u0130\u0099\2\u0597\u0598\7\u00ba\2\2\u0598")
        buf.write(u"\u0599\5\u0126\u0094\2\u0599\u059a\7\u00bb\2\2\u059a")
        buf.write(u"\u059c\3\2\2\2\u059b\u0596\3\2\2\2\u059b\u0597\3\2\2")
        buf.write(u"\2\u059c\u012f\3\2\2\2\u059d\u05a0\5\u0138\u009d\2\u059e")
        buf.write(u"\u05a0\5\u0132\u009a\2\u059f\u059d\3\2\2\2\u059f\u059e")
        buf.write(u"\3\2\2\2\u05a0\u0131\3\2\2\2\u05a1\u05a2\7.\2\2\u05a2")
        buf.write(u"\u05a3\5\u0134\u009b\2\u05a3\u0133\3\2\2\2\u05a4\u05a7")
        buf.write(u"\5\u0136\u009c\2\u05a5\u05a7\5<\37\2\u05a6\u05a4\3\2")
        buf.write(u"\2\2\u05a6\u05a5\3\2\2\2\u05a7\u0135\3\2\2\2\u05a8\u05af")
        buf.write(u"\5<\37\2\u05a9\u05aa\7\u00c1\2\2\u05aa\u05ad\5<\37\2")
        buf.write(u"\u05ab\u05ac\7\u00c1\2\2\u05ac\u05ae\5<\37\2\u05ad\u05ab")
        buf.write(u"\3\2\2\2\u05ad\u05ae\3\2\2\2\u05ae\u05b0\3\2\2\2\u05af")
        buf.write(u"\u05a9\3\2\2\2\u05af\u05b0\3\2\2\2\u05b0\u0137\3\2\2")
        buf.write(u"\2\u05b1\u05b3\7+\2\2\u05b2\u05b4\5\u0142\u00a2\2\u05b3")
        buf.write(u"\u05b2\3\2\2\2\u05b3\u05b4\3\2\2\2\u05b4\u05b5\3\2\2")
        buf.write(u"\2\u05b5\u05b7\5\u013a\u009e\2\u05b6\u05b8\5\u00e4s\2")
        buf.write(u"\u05b7\u05b6\3\2\2\2\u05b7\u05b8\3\2\2\2\u05b8\u0139")
        buf.write(u"\3\2\2\2\u05b9\u05be\5\u013c\u009f\2\u05ba\u05bb\7\u00b3")
        buf.write(u"\2\2\u05bb\u05bd\5\u013c\u009f\2\u05bc\u05ba\3\2\2\2")
        buf.write(u"\u05bd\u05c0\3\2\2\2\u05be\u05bc\3\2\2\2\u05be\u05bf")
        buf.write(u"\3\2\2\2\u05bf\u013b\3\2\2\2\u05c0\u05be\3\2\2\2\u05c1")
        buf.write(u"\u05c4\5\u013e\u00a0\2\u05c2\u05c4\5\u0140\u00a1\2\u05c3")
        buf.write(u"\u05c1\3\2\2\2\u05c3\u05c2\3\2\2\2\u05c4\u013d\3\2\2")
        buf.write(u"\2\u05c5\u05c7\5\u009cO\2\u05c6\u05c8\5\u0146\u00a4\2")
        buf.write(u"\u05c7\u05c6\3\2\2\2\u05c7\u05c8\3\2\2\2\u05c8\u013f")
        buf.write(u"\3\2\2\2\u05c9\u05ca\7\u00ca\2\2\u05ca\u05cc\7\u00c1")
        buf.write(u"\2\2\u05cb\u05c9\3\2\2\2\u05cb\u05cc\3\2\2\2\u05cc\u05cd")
        buf.write(u"\3\2\2\2\u05cd\u05ce\7\u00be\2\2\u05ce\u0141\3\2\2\2")
        buf.write(u"\u05cf\u05d0\t\r\2\2\u05d0\u0143\3\2\2\2\u05d1\u05d2")
        buf.write(u"\5<\37\2\u05d2\u05d3\7\u00c1\2\2\u05d3\u05d5\3\2\2\2")
        buf.write(u"\u05d4\u05d1\3\2\2\2\u05d4\u05d5\3\2\2\2\u05d5\u05d6")
        buf.write(u"\3\2\2\2\u05d6\u05d7\5<\37\2\u05d7\u0145\3\2\2\2\u05d8")
        buf.write(u"\u05da\7\3\2\2\u05d9\u05d8\3\2\2\2\u05d9\u05da\3\2\2")
        buf.write(u"\2\u05da\u05db\3\2\2\2\u05db\u05dc\5<\37\2\u05dc\u0147")
        buf.write(u"\3\2\2\2\u05dd\u05e2\5\u0144\u00a3\2\u05de\u05df\7\u00b3")
        buf.write(u"\2\2\u05df\u05e1\5\u0144\u00a3\2\u05e0\u05de\3\2\2\2")
        buf.write(u"\u05e1\u05e4\3\2\2\2\u05e2\u05e0\3\2\2\2\u05e2\u05e3")
        buf.write(u"\3\2\2\2\u05e3\u0149\3\2\2\2\u05e4\u05e2\3\2\2\2\u05e5")
        buf.write(u"\u05e6\5\u0150\u00a9\2\u05e6\u014b\3\2\2\2\u05e7\u05e8")
        buf.write(u"\5\u0150\u00a9\2\u05e8\u014d\3\2\2\2\u05e9\u05ea\5\u0150")
        buf.write(u"\u00a9\2\u05ea\u014f\3\2\2\2\u05eb\u05ec\7\u00ba\2\2")
        buf.write(u"\u05ec\u05ed\5\u0122\u0092\2\u05ed\u05ee\7\u00bb\2\2")
        buf.write(u"\u05ee\u0151\3\2\2\2\u05ef\u05f6\5\u0154\u00ab\2\u05f0")
        buf.write(u"\u05f6\5\u0158\u00ad\2\u05f1\u05f6\5\u015c\u00af\2\u05f2")
        buf.write(u"\u05f6\5\u0162\u00b2\2\u05f3\u05f6\5\u016a\u00b6\2\u05f4")
        buf.write(u"\u05f6\5\u0174\u00bb\2\u05f5\u05ef\3\2\2\2\u05f5\u05f0")
        buf.write(u"\3\2\2\2\u05f5\u05f1\3\2\2\2\u05f5\u05f2\3\2\2\2\u05f5")
        buf.write(u"\u05f3\3\2\2\2\u05f5\u05f4\3\2\2\2\u05f6\u0153\3\2\2")
        buf.write(u"\2\u05f7\u05f8\5\u00e0q\2\u05f8\u05f9\5\u0156\u00ac\2")
        buf.write(u"\u05f9\u05fa\5\u00e0q\2\u05fa\u0155\3\2\2\2\u05fb\u05fc")
        buf.write(u"\t\16\2\2\u05fc\u0157\3\2\2\2\u05fd\u05fe\5\u00e0q\2")
        buf.write(u"\u05fe\u05ff\5\u015a\u00ae\2\u05ff\u0159\3\2\2\2\u0600")
        buf.write(u"\u0602\7$\2\2\u0601\u0600\3\2\2\2\u0601\u0602\3\2\2\2")
        buf.write(u"\u0602\u0603\3\2\2\2\u0603\u0605\79\2\2\u0604\u0606\t")
        buf.write(u"\17\2\2\u0605\u0604\3\2\2\2\u0605\u0606\3\2\2\2\u0606")
        buf.write(u"\u0607\3\2\2\2\u0607\u0608\5\u00e0q\2\u0608\u0609\7\5")
        buf.write(u"\2\2\u0609\u060a\5\u00e0q\2\u060a\u015b\3\2\2\2\u060b")
        buf.write(u"\u060d\5\u00a0Q\2\u060c\u060e\7$\2\2\u060d\u060c\3\2")
        buf.write(u"\2\2\u060d\u060e\3\2\2\2\u060e\u060f\3\2\2\2\u060f\u0610")
        buf.write(u"\7\31\2\2\u0610\u0611\5\u015e\u00b0\2\u0611\u015d\3\2")
        buf.write(u"\2\2\u0612\u0618\5\u014e\u00a8\2\u0613\u0614\7\u00ba")
        buf.write(u"\2\2\u0614\u0615\5\u0160\u00b1\2\u0615\u0616\7\u00bb")
        buf.write(u"\2\2\u0616\u0618\3\2\2\2\u0617\u0612\3\2\2\2\u0617\u0613")
        buf.write(u"\3\2\2\2\u0618\u015f\3\2\2\2\u0619\u061e\5\u00dan\2\u061a")
        buf.write(u"\u061b\7\u00b3\2\2\u061b\u061d\5\u00dan\2\u061c\u061a")
        buf.write(u"\3\2\2\2\u061d\u0620\3\2\2\2\u061e\u061c\3\2\2\2\u061e")
        buf.write(u"\u061f\3\2\2\2\u061f\u0161\3\2\2\2\u0620\u061e\3\2\2")
        buf.write(u"\2\u0621\u0622\5\u00e0q\2\u0622\u0623\5\u0164\u00b3\2")
        buf.write(u"\u0623\u0624\7\u00cb\2\2\u0624\u0163\3\2\2\2\u0625\u0627")
        buf.write(u"\7$\2\2\u0626\u0625\3\2\2\2\u0626\u0627\3\2\2\2\u0627")
        buf.write(u"\u0628\3\2\2\2\u0628\u062b\5\u0166\u00b4\2\u0629\u062b")
        buf.write(u"\5\u0168\u00b5\2\u062a\u0626\3\2\2\2\u062a\u0629\3\2")
        buf.write(u"\2\2\u062b\u0165\3\2\2\2\u062c\u0633\7!\2\2\u062d\u0633")
        buf.write(u"\7\30\2\2\u062e\u062f\7s\2\2\u062f\u0633\7~\2\2\u0630")
        buf.write(u"\u0633\7n\2\2\u0631\u0633\7o\2\2\u0632\u062c\3\2\2\2")
        buf.write(u"\u0632\u062d\3\2\2\2\u0632\u062e\3\2\2\2\u0632\u0630")
        buf.write(u"\3\2\2\2\u0632\u0631\3\2\2\2\u0633\u0167\3\2\2\2\u0634")
        buf.write(u"\u0635\t\20\2\2\u0635\u0169\3\2\2\2\u0636\u0637\5\u00e0")
        buf.write(u"q\2\u0637\u0639\7\35\2\2\u0638\u063a\7$\2\2\u0639\u0638")
        buf.write(u"\3\2\2\2\u0639\u063a\3\2\2\2\u063a\u063b\3\2\2\2\u063b")
        buf.write(u"\u063c\7%\2\2\u063c\u016b\3\2\2\2\u063d\u063e\5\u00a0")
        buf.write(u"Q\2\u063e\u063f\5\u0156\u00ac\2\u063f\u0640\5\u016e\u00b8")
        buf.write(u"\2\u0640\u0641\5\u014e\u00a8\2\u0641\u016d\3\2\2\2\u0642")
        buf.write(u"\u0645\5\u0170\u00b9\2\u0643\u0645\5\u0172\u00ba\2\u0644")
        buf.write(u"\u0642\3\2\2\2\u0644\u0643\3\2\2\2\u0645\u016f\3\2\2")
        buf.write(u"\2\u0646\u0647\7\4\2\2\u0647\u0171\3\2\2\2\u0648\u0649")
        buf.write(u"\t\21\2\2\u0649\u0173\3\2\2\2\u064a\u064c\7$\2\2\u064b")
        buf.write(u"\u064a\3\2\2\2\u064b\u064c\3\2\2\2\u064c\u064d\3\2\2")
        buf.write(u"\2\u064d\u064e\7J\2\2\u064e\u064f\5\u014e\u00a8\2\u064f")
        buf.write(u"\u0175\3\2\2\2\u0650\u0651\7\63\2\2\u0651\u0652\5\u014e")
        buf.write(u"\u00a8\2\u0652\u0177\3\2\2\2\u0653\u0656\5\u017a\u00be")
        buf.write(u"\2\u0654\u0656\7q\2\2\u0655\u0653\3\2\2\2\u0655\u0654")
        buf.write(u"\3\2\2\2\u0656\u0179\3\2\2\2\u0657\u0658\t\22\2\2\u0658")
        buf.write(u"\u017b\3\2\2\2\u0659\u065a\t\23\2\2\u065a\u017d\3\2\2")
        buf.write(u"\2\u065b\u065c\5\u0182\u00c2\2\u065c\u065e\7\u00ba\2")
        buf.write(u"\2\u065d\u065f\5\u0184\u00c3\2\u065e\u065d\3\2\2\2\u065e")
        buf.write(u"\u065f\3\2\2\2\u065f\u0660\3\2\2\2\u0660\u0661\7\u00bb")
        buf.write(u"\2\2\u0661\u017f\3\2\2\2\u0662\u0663\t\24\2\2\u0663\u0181")
        buf.write(u"\3\2\2\2\u0664\u0667\5<\37\2\u0665\u0667\5\u0180\u00c1")
        buf.write(u"\2\u0666\u0664\3\2\2\2\u0666\u0665\3\2\2\2\u0667\u0183")
        buf.write(u"\3\2\2\2\u0668\u066d\5\u009cO\2\u0669\u066a\7\u00b3\2")
        buf.write(u"\2\u066a\u066c\5\u009cO\2\u066b\u0669\3\2\2\2\u066c\u066f")
        buf.write(u"\3\2\2\2\u066d\u066b\3\2\2\2\u066d\u066e\3\2\2\2\u066e")
        buf.write(u"\u0185\3\2\2\2\u066f\u066d\3\2\2\2\u0670\u0671\7)\2\2")
        buf.write(u"\u0671\u0672\7:\2\2\u0672\u0673\5\u0188\u00c5\2\u0673")
        buf.write(u"\u0187\3\2\2\2\u0674\u0679\5\u018a\u00c6\2\u0675\u0676")
        buf.write(u"\7\u00b3\2\2\u0676\u0678\5\u018a\u00c6\2\u0677\u0675")
        buf.write(u"\3\2\2\2\u0678\u067b\3\2\2\2\u0679\u0677\3\2\2\2\u0679")
        buf.write(u"\u067a\3\2\2\2\u067a\u0189\3\2\2\2\u067b\u0679\3\2\2")
        buf.write(u"\2\u067c\u067e\5\u00e0q\2\u067d\u067f\5\u018c\u00c7\2")
        buf.write(u"\u067e\u067d\3\2\2\2\u067e\u067f\3\2\2\2\u067f\u0681")
        buf.write(u"\3\2\2\2\u0680\u0682\5\u0190\u00c9\2\u0681\u0680\3\2")
        buf.write(u"\2\2\u0681\u0682\3\2\2\2\u0682\u018b\3\2\2\2\u0683\u0684")
        buf.write(u"\t\25\2\2\u0684\u018d\3\2\2\2\u0685\u0686\7\"\2\2\u0686")
        buf.write(u"\u0687\5\u00a0Q\2\u0687\u018f\3\2\2\2\u0688\u0689\7%")
        buf.write(u"\2\2\u0689\u068d\7N\2\2\u068a\u068b\7%\2\2\u068b\u068d")
        buf.write(u"\7Y\2\2\u068c\u0688\3\2\2\2\u068c\u068a\3\2\2\2\u068d")
        buf.write(u"\u0191\3\2\2\2\u068e\u0690\7U\2\2\u068f\u0691\7g\2\2")
        buf.write(u"\u0690\u068f\3\2\2\2\u0690\u0691\3\2\2\2\u0691\u0692")
        buf.write(u"\3\2\2\2\u0692\u0693\7\34\2\2\u0693\u0698\5\u0136\u009c")
        buf.write(u"\2\u0694\u0695\7\u00ba\2\2\u0695\u0696\5\u0106\u0084")
        buf.write(u"\2\u0696\u0697\7\u00bb\2\2\u0697\u0699\3\2\2\2\u0698")
        buf.write(u"\u0694\3\2\2\2\u0698\u0699\3\2\2\2\u0699\u069a\3\2\2")
        buf.write(u"\2\u069a\u069b\5\u0122\u0092\2\u069b\u06ac\3\2\2\2\u069c")
        buf.write(u"\u069e\7U\2\2\u069d\u069f\7g\2\2\u069e\u069d\3\2\2\2")
        buf.write(u"\u069e\u069f\3\2\2\2\u069f\u06a0\3\2\2\2\u06a0\u06a1")
        buf.write(u"\7\34\2\2\u06a1\u06a2\7\\\2\2\u06a2\u06a8\7\u00cb\2\2")
        buf.write(u"\u06a3\u06a4\7\64\2\2\u06a4\u06a6\5<\37\2\u06a5\u06a7")
        buf.write(u"\5\26\f\2\u06a6\u06a5\3\2\2\2\u06a6\u06a7\3\2\2\2\u06a7")
        buf.write(u"\u06a9\3\2\2\2\u06a8\u06a3\3\2\2\2\u06a8\u06a9\3\2\2")
        buf.write(u"\2\u06a9\u06aa\3\2\2\2\u06aa\u06ac\5\u0122\u0092\2\u06ab")
        buf.write(u"\u068e\3\2\2\2\u06ab\u069c\3\2\2\2\u06ac\u0193\3\2\2")
        buf.write(u"\2\u00bc\u0196\u019e\u01a6\u01aa\u01b1\u01b7\u01c1\u01c4")
        buf.write(u"\u01cf\u01d2\u01d5\u01d9\u01e0\u01e3\u01e6\u01eb\u01f3")
        buf.write(u"\u0204\u0219\u022a\u0237\u023b\u023d\u024a\u0251\u0269")
        buf.write(u"\u0270\u0281\u0285\u028b\u0290\u0295\u02ad\u02b3\u02b7")
        buf.write(u"\u02bc\u02c1\u02c5\u02c8\u02d1\u02d6\u02da\u02e0\u02e6")
        buf.write(u"\u02eb\u02ef\u02f1\u02f5\u02f9\u02fb\u02ff\u0303\u0307")
        buf.write(u"\u030b\u0316\u031a\u0322\u032c\u033d\u0341\u0345\u034a")
        buf.write(u"\u034c\u0350\u0355\u0359\u035b\u035f\u036c\u0373\u037f")
        buf.write(u"\u0381\u0386\u03a8\u03ac\u03b0\u03b7\u03ba\u03c2\u03c5")
        buf.write(u"\u03d8\u03e8\u03ed\u03f4\u03fc\u0400\u040a\u0414\u0418")
        buf.write(u"\u0428\u042e\u0437\u043e\u0448\u044b\u044e\u0455\u0460")
        buf.write(u"\u0468\u046e\u0472\u0476\u047e\u0482\u048a\u0492\u0496")
        buf.write(u"\u049a\u049d\u04a0\u04a3\u04a6\u04b0\u04b5\u04bb\u04c1")
        buf.write(u"\u04c9\u04d0\u04d7\u04df\u04ea\u04ee\u04f4\u0500\u0503")
        buf.write(u"\u0509\u050d\u0514\u0516\u051d\u0530\u0537\u053e\u0545")
        buf.write(u"\u055d\u0564\u056a\u056e\u0572\u0577\u057c\u0582\u0586")
        buf.write(u"\u058a\u058f\u0594\u059b\u059f\u05a6\u05ad\u05af\u05b3")
        buf.write(u"\u05b7\u05be\u05c3\u05c7\u05cb\u05d4\u05d9\u05e2\u05f5")
        buf.write(u"\u0601\u0605\u060d\u0617\u061e\u0626\u062a\u0632\u0639")
        buf.write(u"\u0644\u064b\u0655\u065e\u0666\u066d\u0679\u067e\u0681")
        buf.write(u"\u068c\u0690\u0698\u069e\u06a6\u06a8\u06ab")
        return buf.getvalue()


class SQLParser ( Parser ):

    grammarFileName = "SQLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'~'", u"'!~'", u"'~*'", u"'!~*'", u"<INVALID>", u"':='", 
                     u"'='", u"':'", u"';'", u"','", u"<INVALID>", u"<INVALID>", 
                     u"'<'", u"'<='", u"'>'", u"'>='", u"'('", u"')'", u"'+'", 
                     u"'-'", u"'*'", u"'/'", u"'%'", u"'.'", u"'_'", u"'|'", 
                     u"'''", u"'\"'", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"' '" ]

    symbolicNames = [ u"<INVALID>", u"AS", u"ALL", u"AND", u"ANY", u"ASYMMETRIC", 
                      u"ASC", u"BOTH", u"CASE", u"CAST", u"CREATE", u"CROSS", 
                      u"DESC", u"DISTINCT", u"END", u"ELSE", u"EXCEPT", 
                      u"FALSE", u"FULL", u"FROM", u"GROUP", u"HAVING", u"ILIKE", 
                      u"IN", u"INNER", u"INTERSECT", u"INTO", u"IS", u"JOIN", 
                      u"LEADING", u"LEFT", u"LIKE", u"LIMIT", u"NATURAL", 
                      u"NOT", u"NULL", u"ON", u"OUTER", u"OR", u"ORDER", 
                      u"RIGHT", u"SELECT", u"SOME", u"SYMMETRIC", u"TABLE", 
                      u"THEN", u"TRAILING", u"TRUE", u"UNION", u"UNIQUE", 
                      u"USING", u"WHEN", u"WHERE", u"WITH", u"AVG", u"BETWEEN", 
                      u"BY", u"CENTURY", u"CHARACTER", u"COLLECT", u"COALESCE", 
                      u"COLUMN", u"COUNT", u"CUBE", u"DAY", u"DEC", u"DECADE", 
                      u"DOW", u"DOY", u"DROP", u"EPOCH", u"EVERY", u"EXISTS", 
                      u"EXTERNAL", u"EXTRACT", u"FILTER", u"FIRST", u"FORMAT", 
                      u"FUSION", u"GROUPING", u"HASH", u"HOUR", u"INDEX", 
                      u"INSERT", u"INTERSECTION", u"ISODOW", u"ISOYEAR", 
                      u"LAST", u"LESS", u"LIST", u"LOCATION", u"MAX", u"MAXVALUE", 
                      u"MICROSECONDS", u"MILLENNIUM", u"MILLISECONDS", u"MIN", 
                      u"MINUTE", u"MONTH", u"NATIONAL", u"NULLIF", u"OVERWRITE", 
                      u"PARTITION", u"PARTITIONS", u"PRECISION", u"PURGE", 
                      u"QUARTER", u"RANGE", u"REGEXP", u"RLIKE", u"ROLLUP", 
                      u"SECOND", u"SET", u"SIMILAR", u"STDDEV_POP", u"STDDEV_SAMP", 
                      u"SUBPARTITION", u"SUM", u"TABLESPACE", u"THAN", u"TIMEZONE", 
                      u"TIMEZONE_HOUR", u"TIMEZONE_MINUTE", u"TRIM", u"TO", 
                      u"UNKNOWN", u"VALUES", u"VAR_SAMP", u"VAR_POP", u"VARYING", 
                      u"WEEK", u"YEAR", u"ZONE", u"BOOLEAN", u"BOOL", u"BIT", 
                      u"VARBIT", u"INT1", u"INT2", u"INT4", u"INT8", u"TINYINT", 
                      u"SMALLINT", u"INT", u"INTEGER", u"BIGINT", u"FLOAT4", 
                      u"FLOAT8", u"REAL", u"FLOAT", u"DOUBLE", u"NUMERIC", 
                      u"DECIMAL", u"CHAR", u"VARCHAR", u"NCHAR", u"NVARCHAR", 
                      u"DATE", u"TIME", u"TIMETZ", u"TIMESTAMP", u"TIMESTAMPTZ", 
                      u"TEXT", u"BINARY", u"VARBINARY", u"BLOB", u"BYTEA", 
                      u"INET4", u"Similar_To", u"Not_Similar_To", u"Similar_To_Case_Insensitive", 
                      u"Not_Similar_To_Case_Insensitive", u"CAST_EXPRESSION", 
                      u"ASSIGN", u"EQUAL", u"COLON", u"SEMI_COLON", u"COMMA", 
                      u"CONCATENATION_OPERATOR", u"NOT_EQUAL", u"LTH", u"LEQ", 
                      u"GTH", u"GEQ", u"LEFT_PAREN", u"RIGHT_PAREN", u"PLUS", 
                      u"MINUS", u"MULTIPLY", u"DIVIDE", u"MODULAR", u"DOT", 
                      u"UNDERLINE", u"VERTICAL_BAR", u"QUOTE", u"DOUBLE_QUOTE", 
                      u"NUMBER", u"REAL_NUMBER", u"BlockComment", u"LineComment", 
                      u"Identifier", u"Character_String_Literal", u"Space", 
                      u"White_Space", u"BAD" ]

    RULE_sql = 0
    RULE_statement = 1
    RULE_data_statement = 2
    RULE_data_change_statement = 3
    RULE_schema_statement = 4
    RULE_index_statement = 5
    RULE_create_table_statement = 6
    RULE_table_elements = 7
    RULE_field_element = 8
    RULE_field_type = 9
    RULE_param_clause = 10
    RULE_param = 11
    RULE_method_specifier = 12
    RULE_table_space_specifier = 13
    RULE_table_space_name = 14
    RULE_table_partitioning_clauses = 15
    RULE_range_partitions = 16
    RULE_range_value_clause_list = 17
    RULE_range_value_clause = 18
    RULE_hash_partitions = 19
    RULE_individual_hash_partitions = 20
    RULE_individual_hash_partition = 21
    RULE_hash_partitions_by_quantity = 22
    RULE_list_partitions = 23
    RULE_list_value_clause_list = 24
    RULE_list_value_partition = 25
    RULE_column_partitions = 26
    RULE_partition_name = 27
    RULE_drop_table_statement = 28
    RULE_identifier = 29
    RULE_nonreserved_keywords = 30
    RULE_unsigned_literal = 31
    RULE_general_literal = 32
    RULE_datetime_literal = 33
    RULE_time_literal = 34
    RULE_timestamp_literal = 35
    RULE_date_literal = 36
    RULE_boolean_literal = 37
    RULE_data_type = 38
    RULE_predefined_type = 39
    RULE_network_type = 40
    RULE_character_string_type = 41
    RULE_type_length = 42
    RULE_national_character_string_type = 43
    RULE_binary_large_object_string_type = 44
    RULE_numeric_type = 45
    RULE_exact_numeric_type = 46
    RULE_approximate_numeric_type = 47
    RULE_precision_param = 48
    RULE_boolean_type = 49
    RULE_datetime_type = 50
    RULE_bit_type = 51
    RULE_binary_type = 52
    RULE_value_expression_primary = 53
    RULE_parenthesized_value_expression = 54
    RULE_nonparenthesized_value_expression_primary = 55
    RULE_unsigned_value_specification = 56
    RULE_unsigned_numeric_literal = 57
    RULE_signed_numerical_literal = 58
    RULE_set_function_specification = 59
    RULE_aggregate_function = 60
    RULE_general_set_function = 61
    RULE_set_function_type = 62
    RULE_filter_clause = 63
    RULE_grouping_operation = 64
    RULE_case_expression = 65
    RULE_case_abbreviation = 66
    RULE_case_specification = 67
    RULE_simple_case = 68
    RULE_searched_case = 69
    RULE_simple_when_clause = 70
    RULE_searched_when_clause = 71
    RULE_else_clause = 72
    RULE_result = 73
    RULE_cast_specification = 74
    RULE_cast_operand = 75
    RULE_cast_target = 76
    RULE_value_expression = 77
    RULE_common_value_expression = 78
    RULE_numeric_value_expression = 79
    RULE_term = 80
    RULE_factor = 81
    RULE_array = 82
    RULE_numeric_primary = 83
    RULE_sign = 84
    RULE_numeric_value_function = 85
    RULE_extract_expression = 86
    RULE_extract_field = 87
    RULE_time_zone_field = 88
    RULE_extract_source = 89
    RULE_string_value_expression = 90
    RULE_character_value_expression = 91
    RULE_character_factor = 92
    RULE_character_primary = 93
    RULE_string_value_function = 94
    RULE_trim_function = 95
    RULE_trim_operands = 96
    RULE_trim_specification = 97
    RULE_boolean_value_expression = 98
    RULE_or_predicate = 99
    RULE_and_predicate = 100
    RULE_boolean_factor = 101
    RULE_boolean_test = 102
    RULE_is_clause = 103
    RULE_truth_value = 104
    RULE_boolean_primary = 105
    RULE_boolean_predicand = 106
    RULE_parenthesized_boolean_value_expression = 107
    RULE_row_value_expression = 108
    RULE_row_value_special_case = 109
    RULE_explicit_row_value_constructor = 110
    RULE_row_value_predicand = 111
    RULE_row_value_constructor_predicand = 112
    RULE_table_expression = 113
    RULE_from_clause = 114
    RULE_table_reference_list = 115
    RULE_table_reference = 116
    RULE_joined_table = 117
    RULE_joined_table_primary = 118
    RULE_cross_join = 119
    RULE_qualified_join = 120
    RULE_natural_join = 121
    RULE_union_join = 122
    RULE_join_type = 123
    RULE_outer_join_type = 124
    RULE_outer_join_type_part2 = 125
    RULE_join_specification = 126
    RULE_join_condition = 127
    RULE_named_columns_join = 128
    RULE_table_primary = 129
    RULE_column_name_list = 130
    RULE_derived_table = 131
    RULE_where_clause = 132
    RULE_search_condition = 133
    RULE_groupby_clause = 134
    RULE_grouping_element_list = 135
    RULE_grouping_element = 136
    RULE_ordinary_grouping_set = 137
    RULE_ordinary_grouping_set_list = 138
    RULE_rollup_list = 139
    RULE_cube_list = 140
    RULE_empty_grouping_set = 141
    RULE_having_clause = 142
    RULE_row_value_predicand_list = 143
    RULE_query_expression = 144
    RULE_query_expression_body = 145
    RULE_non_join_query_expression = 146
    RULE_query_term = 147
    RULE_non_join_query_term = 148
    RULE_query_primary = 149
    RULE_non_join_query_primary = 150
    RULE_simple_table = 151
    RULE_explicit_table = 152
    RULE_table_or_query_name = 153
    RULE_table_name = 154
    RULE_query_specification = 155
    RULE_select_list = 156
    RULE_select_sublist = 157
    RULE_derived_column = 158
    RULE_qualified_asterisk = 159
    RULE_set_qualifier = 160
    RULE_column_reference = 161
    RULE_as_clause = 162
    RULE_column_reference_list = 163
    RULE_scalar_subquery = 164
    RULE_row_subquery = 165
    RULE_table_subquery = 166
    RULE_subquery = 167
    RULE_predicate = 168
    RULE_comparison_predicate = 169
    RULE_comp_op = 170
    RULE_between_predicate = 171
    RULE_between_predicate_part_2 = 172
    RULE_in_predicate = 173
    RULE_in_predicate_value = 174
    RULE_in_value_list = 175
    RULE_pattern_matching_predicate = 176
    RULE_pattern_matcher = 177
    RULE_negativable_matcher = 178
    RULE_regex_matcher = 179
    RULE_null_predicate = 180
    RULE_quantified_comparison_predicate = 181
    RULE_quantifier = 182
    RULE_all = 183
    RULE_some = 184
    RULE_exists_predicate = 185
    RULE_unique_predicate = 186
    RULE_primary_datetime_field = 187
    RULE_non_second_primary_datetime_field = 188
    RULE_extended_datetime_field = 189
    RULE_routine_invocation = 190
    RULE_function_names_for_reserved_words = 191
    RULE_function_name = 192
    RULE_sql_argument_list = 193
    RULE_orderby_clause = 194
    RULE_sort_specifier_list = 195
    RULE_sort_specifier = 196
    RULE_order_specification = 197
    RULE_limit_clause = 198
    RULE_null_ordering = 199
    RULE_insert_statement = 200

    ruleNames =  [ u"sql", u"statement", u"data_statement", u"data_change_statement", 
                   u"schema_statement", u"index_statement", u"create_table_statement", 
                   u"table_elements", u"field_element", u"field_type", u"param_clause", 
                   u"param", u"method_specifier", u"table_space_specifier", 
                   u"table_space_name", u"table_partitioning_clauses", u"range_partitions", 
                   u"range_value_clause_list", u"range_value_clause", u"hash_partitions", 
                   u"individual_hash_partitions", u"individual_hash_partition", 
                   u"hash_partitions_by_quantity", u"list_partitions", u"list_value_clause_list", 
                   u"list_value_partition", u"column_partitions", u"partition_name", 
                   u"drop_table_statement", u"identifier", u"nonreserved_keywords", 
                   u"unsigned_literal", u"general_literal", u"datetime_literal", 
                   u"time_literal", u"timestamp_literal", u"date_literal", 
                   u"boolean_literal", u"data_type", u"predefined_type", 
                   u"network_type", u"character_string_type", u"type_length", 
                   u"national_character_string_type", u"binary_large_object_string_type", 
                   u"numeric_type", u"exact_numeric_type", u"approximate_numeric_type", 
                   u"precision_param", u"boolean_type", u"datetime_type", 
                   u"bit_type", u"binary_type", u"value_expression_primary", 
                   u"parenthesized_value_expression", u"nonparenthesized_value_expression_primary", 
                   u"unsigned_value_specification", u"unsigned_numeric_literal", 
                   u"signed_numerical_literal", u"set_function_specification", 
                   u"aggregate_function", u"general_set_function", u"set_function_type", 
                   u"filter_clause", u"grouping_operation", u"case_expression", 
                   u"case_abbreviation", u"case_specification", u"simple_case", 
                   u"searched_case", u"simple_when_clause", u"searched_when_clause", 
                   u"else_clause", u"result", u"cast_specification", u"cast_operand", 
                   u"cast_target", u"value_expression", u"common_value_expression", 
                   u"numeric_value_expression", u"term", u"factor", u"array", 
                   u"numeric_primary", u"sign", u"numeric_value_function", 
                   u"extract_expression", u"extract_field", u"time_zone_field", 
                   u"extract_source", u"string_value_expression", u"character_value_expression", 
                   u"character_factor", u"character_primary", u"string_value_function", 
                   u"trim_function", u"trim_operands", u"trim_specification", 
                   u"boolean_value_expression", u"or_predicate", u"and_predicate", 
                   u"boolean_factor", u"boolean_test", u"is_clause", u"truth_value", 
                   u"boolean_primary", u"boolean_predicand", u"parenthesized_boolean_value_expression", 
                   u"row_value_expression", u"row_value_special_case", u"explicit_row_value_constructor", 
                   u"row_value_predicand", u"row_value_constructor_predicand", 
                   u"table_expression", u"from_clause", u"table_reference_list", 
                   u"table_reference", u"joined_table", u"joined_table_primary", 
                   u"cross_join", u"qualified_join", u"natural_join", u"union_join", 
                   u"join_type", u"outer_join_type", u"outer_join_type_part2", 
                   u"join_specification", u"join_condition", u"named_columns_join", 
                   u"table_primary", u"column_name_list", u"derived_table", 
                   u"where_clause", u"search_condition", u"groupby_clause", 
                   u"grouping_element_list", u"grouping_element", u"ordinary_grouping_set", 
                   u"ordinary_grouping_set_list", u"rollup_list", u"cube_list", 
                   u"empty_grouping_set", u"having_clause", u"row_value_predicand_list", 
                   u"query_expression", u"query_expression_body", u"non_join_query_expression", 
                   u"query_term", u"non_join_query_term", u"query_primary", 
                   u"non_join_query_primary", u"simple_table", u"explicit_table", 
                   u"table_or_query_name", u"table_name", u"query_specification", 
                   u"select_list", u"select_sublist", u"derived_column", 
                   u"qualified_asterisk", u"set_qualifier", u"column_reference", 
                   u"as_clause", u"column_reference_list", u"scalar_subquery", 
                   u"row_subquery", u"table_subquery", u"subquery", u"predicate", 
                   u"comparison_predicate", u"comp_op", u"between_predicate", 
                   u"between_predicate_part_2", u"in_predicate", u"in_predicate_value", 
                   u"in_value_list", u"pattern_matching_predicate", u"pattern_matcher", 
                   u"negativable_matcher", u"regex_matcher", u"null_predicate", 
                   u"quantified_comparison_predicate", u"quantifier", u"all", 
                   u"some", u"exists_predicate", u"unique_predicate", u"primary_datetime_field", 
                   u"non_second_primary_datetime_field", u"extended_datetime_field", 
                   u"routine_invocation", u"function_names_for_reserved_words", 
                   u"function_name", u"sql_argument_list", u"orderby_clause", 
                   u"sort_specifier_list", u"sort_specifier", u"order_specification", 
                   u"limit_clause", u"null_ordering", u"insert_statement" ]

    EOF = Token.EOF
    AS=1
    ALL=2
    AND=3
    ANY=4
    ASYMMETRIC=5
    ASC=6
    BOTH=7
    CASE=8
    CAST=9
    CREATE=10
    CROSS=11
    DESC=12
    DISTINCT=13
    END=14
    ELSE=15
    EXCEPT=16
    FALSE=17
    FULL=18
    FROM=19
    GROUP=20
    HAVING=21
    ILIKE=22
    IN=23
    INNER=24
    INTERSECT=25
    INTO=26
    IS=27
    JOIN=28
    LEADING=29
    LEFT=30
    LIKE=31
    LIMIT=32
    NATURAL=33
    NOT=34
    NULL=35
    ON=36
    OUTER=37
    OR=38
    ORDER=39
    RIGHT=40
    SELECT=41
    SOME=42
    SYMMETRIC=43
    TABLE=44
    THEN=45
    TRAILING=46
    TRUE=47
    UNION=48
    UNIQUE=49
    USING=50
    WHEN=51
    WHERE=52
    WITH=53
    AVG=54
    BETWEEN=55
    BY=56
    CENTURY=57
    CHARACTER=58
    COLLECT=59
    COALESCE=60
    COLUMN=61
    COUNT=62
    CUBE=63
    DAY=64
    DEC=65
    DECADE=66
    DOW=67
    DOY=68
    DROP=69
    EPOCH=70
    EVERY=71
    EXISTS=72
    EXTERNAL=73
    EXTRACT=74
    FILTER=75
    FIRST=76
    FORMAT=77
    FUSION=78
    GROUPING=79
    HASH=80
    HOUR=81
    INDEX=82
    INSERT=83
    INTERSECTION=84
    ISODOW=85
    ISOYEAR=86
    LAST=87
    LESS=88
    LIST=89
    LOCATION=90
    MAX=91
    MAXVALUE=92
    MICROSECONDS=93
    MILLENNIUM=94
    MILLISECONDS=95
    MIN=96
    MINUTE=97
    MONTH=98
    NATIONAL=99
    NULLIF=100
    OVERWRITE=101
    PARTITION=102
    PARTITIONS=103
    PRECISION=104
    PURGE=105
    QUARTER=106
    RANGE=107
    REGEXP=108
    RLIKE=109
    ROLLUP=110
    SECOND=111
    SET=112
    SIMILAR=113
    STDDEV_POP=114
    STDDEV_SAMP=115
    SUBPARTITION=116
    SUM=117
    TABLESPACE=118
    THAN=119
    TIMEZONE=120
    TIMEZONE_HOUR=121
    TIMEZONE_MINUTE=122
    TRIM=123
    TO=124
    UNKNOWN=125
    VALUES=126
    VAR_SAMP=127
    VAR_POP=128
    VARYING=129
    WEEK=130
    YEAR=131
    ZONE=132
    BOOLEAN=133
    BOOL=134
    BIT=135
    VARBIT=136
    INT1=137
    INT2=138
    INT4=139
    INT8=140
    TINYINT=141
    SMALLINT=142
    INT=143
    INTEGER=144
    BIGINT=145
    FLOAT4=146
    FLOAT8=147
    REAL=148
    FLOAT=149
    DOUBLE=150
    NUMERIC=151
    DECIMAL=152
    CHAR=153
    VARCHAR=154
    NCHAR=155
    NVARCHAR=156
    DATE=157
    TIME=158
    TIMETZ=159
    TIMESTAMP=160
    TIMESTAMPTZ=161
    TEXT=162
    BINARY=163
    VARBINARY=164
    BLOB=165
    BYTEA=166
    INET4=167
    Similar_To=168
    Not_Similar_To=169
    Similar_To_Case_Insensitive=170
    Not_Similar_To_Case_Insensitive=171
    CAST_EXPRESSION=172
    ASSIGN=173
    EQUAL=174
    COLON=175
    SEMI_COLON=176
    COMMA=177
    CONCATENATION_OPERATOR=178
    NOT_EQUAL=179
    LTH=180
    LEQ=181
    GTH=182
    GEQ=183
    LEFT_PAREN=184
    RIGHT_PAREN=185
    PLUS=186
    MINUS=187
    MULTIPLY=188
    DIVIDE=189
    MODULAR=190
    DOT=191
    UNDERLINE=192
    VERTICAL_BAR=193
    QUOTE=194
    DOUBLE_QUOTE=195
    NUMBER=196
    REAL_NUMBER=197
    BlockComment=198
    LineComment=199
    Identifier=200
    Character_String_Literal=201
    Space=202
    White_Space=203
    BAD=204

    def __init__(self, input, output=sys.stdout):
        super(SQLParser, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None





    class SqlContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.SqlContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(SQLParser.StatementContext,0)


        def EOF(self):
            return self.getToken(SQLParser.EOF, 0)

        def SEMI_COLON(self):
            return self.getToken(SQLParser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_sql

        def accept(self, visitor):
            if hasattr(visitor, "visitSql"):
                return visitor.visitSql(self)
            else:
                return visitor.visitChildren(self)




    def sql(self):

        localctx = SQLParser.SqlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sql)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.statement()
            self.state = 404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.SEMI_COLON:
                self.state = 403
                self.match(SQLParser.SEMI_COLON)


            self.state = 406
            self.match(SQLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def data_statement(self):
            return self.getTypedRuleContext(SQLParser.Data_statementContext,0)


        def data_change_statement(self):
            return self.getTypedRuleContext(SQLParser.Data_change_statementContext,0)


        def schema_statement(self):
            return self.getTypedRuleContext(SQLParser.Schema_statementContext,0)


        def index_statement(self):
            return self.getTypedRuleContext(SQLParser.Index_statementContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_statement

        def accept(self, visitor):
            if hasattr(visitor, "visitStatement"):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SQLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.data_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                self.data_change_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 410
                self.schema_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 411
                self.index_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Data_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Data_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def query_expression(self):
            return self.getTypedRuleContext(SQLParser.Query_expressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_data_statement

        def accept(self, visitor):
            if hasattr(visitor, "visitData_statement"):
                return visitor.visitData_statement(self)
            else:
                return visitor.visitChildren(self)




    def data_statement(self):

        localctx = SQLParser.Data_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_data_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.query_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Data_change_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Data_change_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def insert_statement(self):
            return self.getTypedRuleContext(SQLParser.Insert_statementContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_data_change_statement

        def accept(self, visitor):
            if hasattr(visitor, "visitData_change_statement"):
                return visitor.visitData_change_statement(self)
            else:
                return visitor.visitChildren(self)




    def data_change_statement(self):

        localctx = SQLParser.Data_change_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_data_change_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.insert_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Schema_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Schema_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def create_table_statement(self):
            return self.getTypedRuleContext(SQLParser.Create_table_statementContext,0)


        def drop_table_statement(self):
            return self.getTypedRuleContext(SQLParser.Drop_table_statementContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_schema_statement

        def accept(self, visitor):
            if hasattr(visitor, "visitSchema_statement"):
                return visitor.visitSchema_statement(self)
            else:
                return visitor.visitChildren(self)




    def schema_statement(self):

        localctx = SQLParser.Schema_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_schema_statement)
        try:
            self.state = 420
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.CREATE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.create_table_statement()
                pass
            elif token in [SQLParser.DROP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                self.drop_table_statement()
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

    class Index_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Index_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.u = None # Token
            self.n = None # IdentifierContext
            self.t = None # Table_nameContext
            self.m = None # Method_specifierContext
            self.s = None # Sort_specifier_listContext
            self.p = None # Param_clauseContext

        def CREATE(self):
            return self.getToken(SQLParser.CREATE, 0)

        def INDEX(self):
            return self.getToken(SQLParser.INDEX, 0)

        def ON(self):
            return self.getToken(SQLParser.ON, 0)

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def table_name(self):
            return self.getTypedRuleContext(SQLParser.Table_nameContext,0)


        def sort_specifier_list(self):
            return self.getTypedRuleContext(SQLParser.Sort_specifier_listContext,0)


        def UNIQUE(self):
            return self.getToken(SQLParser.UNIQUE, 0)

        def method_specifier(self):
            return self.getTypedRuleContext(SQLParser.Method_specifierContext,0)


        def param_clause(self):
            return self.getTypedRuleContext(SQLParser.Param_clauseContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_index_statement

        def accept(self, visitor):
            if hasattr(visitor, "visitIndex_statement"):
                return visitor.visitIndex_statement(self)
            else:
                return visitor.visitChildren(self)




    def index_statement(self):

        localctx = SQLParser.Index_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_index_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(SQLParser.CREATE)
            self.state = 424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.UNIQUE:
                self.state = 423
                localctx.u = self.match(SQLParser.UNIQUE)


            self.state = 426
            self.match(SQLParser.INDEX)
            self.state = 427
            localctx.n = self.identifier()
            self.state = 428
            self.match(SQLParser.ON)
            self.state = 429
            localctx.t = self.table_name()
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.USING:
                self.state = 430
                localctx.m = self.method_specifier()


            self.state = 433
            self.match(SQLParser.LEFT_PAREN)
            self.state = 434
            localctx.s = self.sort_specifier_list()
            self.state = 435
            self.match(SQLParser.RIGHT_PAREN)
            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.WITH:
                self.state = 436
                localctx.p = self.param_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Create_table_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Create_table_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.file_type = None # IdentifierContext
            self.path = None # Token

        def CREATE(self):
            return self.getToken(SQLParser.CREATE, 0)

        def EXTERNAL(self):
            return self.getToken(SQLParser.EXTERNAL, 0)

        def TABLE(self):
            return self.getToken(SQLParser.TABLE, 0)

        def table_name(self):
            return self.getTypedRuleContext(SQLParser.Table_nameContext,0)


        def table_elements(self):
            return self.getTypedRuleContext(SQLParser.Table_elementsContext,0)


        def USING(self):
            return self.getToken(SQLParser.USING, 0)

        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def LOCATION(self):
            return self.getToken(SQLParser.LOCATION, 0)

        def param_clause(self):
            return self.getTypedRuleContext(SQLParser.Param_clauseContext,0)


        def table_partitioning_clauses(self):
            return self.getTypedRuleContext(SQLParser.Table_partitioning_clausesContext,0)


        def Character_String_Literal(self):
            return self.getToken(SQLParser.Character_String_Literal, 0)

        def AS(self):
            return self.getToken(SQLParser.AS, 0)

        def query_expression(self):
            return self.getTypedRuleContext(SQLParser.Query_expressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_create_table_statement

        def accept(self, visitor):
            if hasattr(visitor, "visitCreate_table_statement"):
                return visitor.visitCreate_table_statement(self)
            else:
                return visitor.visitChildren(self)




    def create_table_statement(self):

        localctx = SQLParser.Create_table_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_create_table_statement)
        self._la = 0 # Token type
        try:
            self.state = 489
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.match(SQLParser.CREATE)
                self.state = 440
                self.match(SQLParser.EXTERNAL)
                self.state = 441
                self.match(SQLParser.TABLE)
                self.state = 442
                self.table_name()
                self.state = 443
                self.table_elements()
                self.state = 444
                self.match(SQLParser.USING)
                self.state = 445
                localctx.file_type = self.identifier()
                self.state = 447
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.WITH:
                    self.state = 446
                    self.param_clause()


                self.state = 450
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.PARTITION:
                    self.state = 449
                    self.table_partitioning_clauses()


                self.state = 452
                self.match(SQLParser.LOCATION)
                self.state = 453
                localctx.path = self.match(SQLParser.Character_String_Literal)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 455
                self.match(SQLParser.CREATE)
                self.state = 456
                self.match(SQLParser.TABLE)
                self.state = 457
                self.table_name()
                self.state = 458
                self.table_elements()
                self.state = 461
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.USING:
                    self.state = 459
                    self.match(SQLParser.USING)
                    self.state = 460
                    localctx.file_type = self.identifier()


                self.state = 464
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.WITH:
                    self.state = 463
                    self.param_clause()


                self.state = 467
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.PARTITION:
                    self.state = 466
                    self.table_partitioning_clauses()


                self.state = 471
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.AS:
                    self.state = 469
                    self.match(SQLParser.AS)
                    self.state = 470
                    self.query_expression()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 473
                self.match(SQLParser.CREATE)
                self.state = 474
                self.match(SQLParser.TABLE)
                self.state = 475
                self.table_name()
                self.state = 478
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.USING:
                    self.state = 476
                    self.match(SQLParser.USING)
                    self.state = 477
                    localctx.file_type = self.identifier()


                self.state = 481
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.WITH:
                    self.state = 480
                    self.param_clause()


                self.state = 484
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.PARTITION:
                    self.state = 483
                    self.table_partitioning_clauses()


                self.state = 486
                self.match(SQLParser.AS)
                self.state = 487
                self.query_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Table_elementsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Table_elementsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def field_element(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Field_elementContext)
            else:
                return self.getTypedRuleContext(SQLParser.Field_elementContext,i)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_table_elements

        def accept(self, visitor):
            if hasattr(visitor, "visitTable_elements"):
                return visitor.visitTable_elements(self)
            else:
                return visitor.visitChildren(self)




    def table_elements(self):

        localctx = SQLParser.Table_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_table_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(SQLParser.LEFT_PAREN)
            self.state = 492
            self.field_element()
            self.state = 497
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.COMMA:
                self.state = 493
                self.match(SQLParser.COMMA)
                self.state = 494
                self.field_element()
                self.state = 499
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 500
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_elementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Field_elementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # IdentifierContext

        def field_type(self):
            return self.getTypedRuleContext(SQLParser.Field_typeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_field_element

        def accept(self, visitor):
            if hasattr(visitor, "visitField_element"):
                return visitor.visitField_element(self)
            else:
                return visitor.visitChildren(self)




    def field_element(self):

        localctx = SQLParser.Field_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_field_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            localctx.name = self.identifier()
            self.state = 503
            self.field_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Field_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def data_type(self):
            return self.getTypedRuleContext(SQLParser.Data_typeContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_field_type

        def accept(self, visitor):
            if hasattr(visitor, "visitField_type"):
                return visitor.visitField_type(self)
            else:
                return visitor.visitChildren(self)




    def field_type(self):

        localctx = SQLParser.Field_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_field_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Param_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Param_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WITH(self):
            return self.getToken(SQLParser.WITH, 0)

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def param(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ParamContext)
            else:
                return self.getTypedRuleContext(SQLParser.ParamContext,i)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_param_clause

        def accept(self, visitor):
            if hasattr(visitor, "visitParam_clause"):
                return visitor.visitParam_clause(self)
            else:
                return visitor.visitChildren(self)




    def param_clause(self):

        localctx = SQLParser.Param_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_param_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(SQLParser.WITH)
            self.state = 508
            self.match(SQLParser.LEFT_PAREN)
            self.state = 509
            self.param()
            self.state = 514
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.COMMA:
                self.state = 510
                self.match(SQLParser.COMMA)
                self.state = 511
                self.param()
                self.state = 516
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 517
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.ParamContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.key = None # Token
            self.value = None # Numeric_value_expressionContext

        def EQUAL(self):
            return self.getToken(SQLParser.EQUAL, 0)

        def Character_String_Literal(self):
            return self.getToken(SQLParser.Character_String_Literal, 0)

        def numeric_value_expression(self):
            return self.getTypedRuleContext(SQLParser.Numeric_value_expressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_param

        def accept(self, visitor):
            if hasattr(visitor, "visitParam"):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = SQLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            localctx.key = self.match(SQLParser.Character_String_Literal)
            self.state = 520
            self.match(SQLParser.EQUAL)
            self.state = 521
            localctx.value = self.numeric_value_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_specifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Method_specifierContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.m = None # IdentifierContext

        def USING(self):
            return self.getToken(SQLParser.USING, 0)

        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_method_specifier

        def accept(self, visitor):
            if hasattr(visitor, "visitMethod_specifier"):
                return visitor.visitMethod_specifier(self)
            else:
                return visitor.visitChildren(self)




    def method_specifier(self):

        localctx = SQLParser.Method_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method_specifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(SQLParser.USING)
            self.state = 524
            localctx.m = self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Table_space_specifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Table_space_specifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TABLESPACE(self):
            return self.getToken(SQLParser.TABLESPACE, 0)

        def table_space_name(self):
            return self.getTypedRuleContext(SQLParser.Table_space_nameContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_table_space_specifier

        def accept(self, visitor):
            if hasattr(visitor, "visitTable_space_specifier"):
                return visitor.visitTable_space_specifier(self)
            else:
                return visitor.visitChildren(self)




    def table_space_specifier(self):

        localctx = SQLParser.Table_space_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_table_space_specifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.match(SQLParser.TABLESPACE)
            self.state = 527
            self.table_space_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Table_space_nameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Table_space_nameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_table_space_name

        def accept(self, visitor):
            if hasattr(visitor, "visitTable_space_name"):
                return visitor.visitTable_space_name(self)
            else:
                return visitor.visitChildren(self)




    def table_space_name(self):

        localctx = SQLParser.Table_space_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_table_space_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Table_partitioning_clausesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Table_partitioning_clausesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def range_partitions(self):
            return self.getTypedRuleContext(SQLParser.Range_partitionsContext,0)


        def hash_partitions(self):
            return self.getTypedRuleContext(SQLParser.Hash_partitionsContext,0)


        def list_partitions(self):
            return self.getTypedRuleContext(SQLParser.List_partitionsContext,0)


        def column_partitions(self):
            return self.getTypedRuleContext(SQLParser.Column_partitionsContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_table_partitioning_clauses

        def accept(self, visitor):
            if hasattr(visitor, "visitTable_partitioning_clauses"):
                return visitor.visitTable_partitioning_clauses(self)
            else:
                return visitor.visitChildren(self)




    def table_partitioning_clauses(self):

        localctx = SQLParser.Table_partitioning_clausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_table_partitioning_clauses)
        try:
            self.state = 535
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 531
                self.range_partitions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 532
                self.hash_partitions()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 533
                self.list_partitions()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 534
                self.column_partitions()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Range_partitionsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Range_partitionsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PARTITION(self):
            return self.getToken(SQLParser.PARTITION, 0)

        def BY(self):
            return self.getToken(SQLParser.BY, 0)

        def RANGE(self):
            return self.getToken(SQLParser.RANGE, 0)

        def LEFT_PAREN(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.LEFT_PAREN)
            else:
                return self.getToken(SQLParser.LEFT_PAREN, i)

        def column_reference_list(self):
            return self.getTypedRuleContext(SQLParser.Column_reference_listContext,0)


        def RIGHT_PAREN(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.RIGHT_PAREN)
            else:
                return self.getToken(SQLParser.RIGHT_PAREN, i)

        def range_value_clause_list(self):
            return self.getTypedRuleContext(SQLParser.Range_value_clause_listContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_range_partitions

        def accept(self, visitor):
            if hasattr(visitor, "visitRange_partitions"):
                return visitor.visitRange_partitions(self)
            else:
                return visitor.visitChildren(self)




    def range_partitions(self):

        localctx = SQLParser.Range_partitionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_range_partitions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.match(SQLParser.PARTITION)
            self.state = 538
            self.match(SQLParser.BY)
            self.state = 539
            self.match(SQLParser.RANGE)
            self.state = 540
            self.match(SQLParser.LEFT_PAREN)
            self.state = 541
            self.column_reference_list()
            self.state = 542
            self.match(SQLParser.RIGHT_PAREN)
            self.state = 543
            self.match(SQLParser.LEFT_PAREN)
            self.state = 544
            self.range_value_clause_list()
            self.state = 545
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Range_value_clause_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Range_value_clause_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def range_value_clause(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Range_value_clauseContext)
            else:
                return self.getTypedRuleContext(SQLParser.Range_value_clauseContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_range_value_clause_list

        def accept(self, visitor):
            if hasattr(visitor, "visitRange_value_clause_list"):
                return visitor.visitRange_value_clause_list(self)
            else:
                return visitor.visitChildren(self)




    def range_value_clause_list(self):

        localctx = SQLParser.Range_value_clause_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_range_value_clause_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.range_value_clause()
            self.state = 552
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.COMMA:
                self.state = 548
                self.match(SQLParser.COMMA)
                self.state = 549
                self.range_value_clause()
                self.state = 554
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Range_value_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Range_value_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PARTITION(self):
            return self.getToken(SQLParser.PARTITION, 0)

        def partition_name(self):
            return self.getTypedRuleContext(SQLParser.Partition_nameContext,0)


        def VALUES(self):
            return self.getToken(SQLParser.VALUES, 0)

        def LESS(self):
            return self.getToken(SQLParser.LESS, 0)

        def THAN(self):
            return self.getToken(SQLParser.THAN, 0)

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def value_expression(self):
            return self.getTypedRuleContext(SQLParser.Value_expressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def MAXVALUE(self):
            return self.getToken(SQLParser.MAXVALUE, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_range_value_clause

        def accept(self, visitor):
            if hasattr(visitor, "visitRange_value_clause"):
                return visitor.visitRange_value_clause(self)
            else:
                return visitor.visitChildren(self)




    def range_value_clause(self):

        localctx = SQLParser.Range_value_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_range_value_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 555
            self.match(SQLParser.PARTITION)
            self.state = 556
            self.partition_name()
            self.state = 557
            self.match(SQLParser.VALUES)
            self.state = 558
            self.match(SQLParser.LESS)
            self.state = 559
            self.match(SQLParser.THAN)
            self.state = 571
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 560
                self.match(SQLParser.LEFT_PAREN)
                self.state = 561
                self.value_expression()
                self.state = 562
                self.match(SQLParser.RIGHT_PAREN)
                pass

            elif la_ == 2:
                self.state = 565
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 564
                    self.match(SQLParser.LEFT_PAREN)


                self.state = 567
                self.match(SQLParser.MAXVALUE)
                self.state = 569
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 568
                    self.match(SQLParser.RIGHT_PAREN)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Hash_partitionsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Hash_partitionsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PARTITION(self):
            return self.getToken(SQLParser.PARTITION, 0)

        def BY(self):
            return self.getToken(SQLParser.BY, 0)

        def HASH(self):
            return self.getToken(SQLParser.HASH, 0)

        def LEFT_PAREN(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.LEFT_PAREN)
            else:
                return self.getToken(SQLParser.LEFT_PAREN, i)

        def column_reference_list(self):
            return self.getTypedRuleContext(SQLParser.Column_reference_listContext,0)


        def RIGHT_PAREN(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.RIGHT_PAREN)
            else:
                return self.getToken(SQLParser.RIGHT_PAREN, i)

        def individual_hash_partitions(self):
            return self.getTypedRuleContext(SQLParser.Individual_hash_partitionsContext,0)


        def hash_partitions_by_quantity(self):
            return self.getTypedRuleContext(SQLParser.Hash_partitions_by_quantityContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_hash_partitions

        def accept(self, visitor):
            if hasattr(visitor, "visitHash_partitions"):
                return visitor.visitHash_partitions(self)
            else:
                return visitor.visitChildren(self)




    def hash_partitions(self):

        localctx = SQLParser.Hash_partitionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_hash_partitions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 573
            self.match(SQLParser.PARTITION)
            self.state = 574
            self.match(SQLParser.BY)
            self.state = 575
            self.match(SQLParser.HASH)
            self.state = 576
            self.match(SQLParser.LEFT_PAREN)
            self.state = 577
            self.column_reference_list()
            self.state = 578
            self.match(SQLParser.RIGHT_PAREN)
            self.state = 584
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.LEFT_PAREN]:
                self.state = 579
                self.match(SQLParser.LEFT_PAREN)
                self.state = 580
                self.individual_hash_partitions()
                self.state = 581
                self.match(SQLParser.RIGHT_PAREN)
                pass
            elif token in [SQLParser.PARTITIONS]:
                self.state = 583
                self.hash_partitions_by_quantity()
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

    class Individual_hash_partitionsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Individual_hash_partitionsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def individual_hash_partition(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Individual_hash_partitionContext)
            else:
                return self.getTypedRuleContext(SQLParser.Individual_hash_partitionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_individual_hash_partitions

        def accept(self, visitor):
            if hasattr(visitor, "visitIndividual_hash_partitions"):
                return visitor.visitIndividual_hash_partitions(self)
            else:
                return visitor.visitChildren(self)




    def individual_hash_partitions(self):

        localctx = SQLParser.Individual_hash_partitionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_individual_hash_partitions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            self.individual_hash_partition()
            self.state = 591
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.COMMA:
                self.state = 587
                self.match(SQLParser.COMMA)
                self.state = 588
                self.individual_hash_partition()
                self.state = 593
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Individual_hash_partitionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Individual_hash_partitionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PARTITION(self):
            return self.getToken(SQLParser.PARTITION, 0)

        def partition_name(self):
            return self.getTypedRuleContext(SQLParser.Partition_nameContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_individual_hash_partition

        def accept(self, visitor):
            if hasattr(visitor, "visitIndividual_hash_partition"):
                return visitor.visitIndividual_hash_partition(self)
            else:
                return visitor.visitChildren(self)




    def individual_hash_partition(self):

        localctx = SQLParser.Individual_hash_partitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_individual_hash_partition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.match(SQLParser.PARTITION)
            self.state = 595
            self.partition_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Hash_partitions_by_quantityContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Hash_partitions_by_quantityContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.quantity = None # Numeric_value_expressionContext

        def PARTITIONS(self):
            return self.getToken(SQLParser.PARTITIONS, 0)

        def numeric_value_expression(self):
            return self.getTypedRuleContext(SQLParser.Numeric_value_expressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_hash_partitions_by_quantity

        def accept(self, visitor):
            if hasattr(visitor, "visitHash_partitions_by_quantity"):
                return visitor.visitHash_partitions_by_quantity(self)
            else:
                return visitor.visitChildren(self)




    def hash_partitions_by_quantity(self):

        localctx = SQLParser.Hash_partitions_by_quantityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_hash_partitions_by_quantity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
            self.match(SQLParser.PARTITIONS)
            self.state = 598
            localctx.quantity = self.numeric_value_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class List_partitionsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.List_partitionsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PARTITION(self):
            return self.getToken(SQLParser.PARTITION, 0)

        def BY(self):
            return self.getToken(SQLParser.BY, 0)

        def LIST(self):
            return self.getToken(SQLParser.LIST, 0)

        def LEFT_PAREN(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.LEFT_PAREN)
            else:
                return self.getToken(SQLParser.LEFT_PAREN, i)

        def column_reference_list(self):
            return self.getTypedRuleContext(SQLParser.Column_reference_listContext,0)


        def RIGHT_PAREN(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.RIGHT_PAREN)
            else:
                return self.getToken(SQLParser.RIGHT_PAREN, i)

        def list_value_clause_list(self):
            return self.getTypedRuleContext(SQLParser.List_value_clause_listContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_list_partitions

        def accept(self, visitor):
            if hasattr(visitor, "visitList_partitions"):
                return visitor.visitList_partitions(self)
            else:
                return visitor.visitChildren(self)




    def list_partitions(self):

        localctx = SQLParser.List_partitionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_list_partitions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 600
            self.match(SQLParser.PARTITION)
            self.state = 601
            self.match(SQLParser.BY)
            self.state = 602
            self.match(SQLParser.LIST)
            self.state = 603
            self.match(SQLParser.LEFT_PAREN)
            self.state = 604
            self.column_reference_list()
            self.state = 605
            self.match(SQLParser.RIGHT_PAREN)
            self.state = 606
            self.match(SQLParser.LEFT_PAREN)
            self.state = 607
            self.list_value_clause_list()
            self.state = 608
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class List_value_clause_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.List_value_clause_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def list_value_partition(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.List_value_partitionContext)
            else:
                return self.getTypedRuleContext(SQLParser.List_value_partitionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_list_value_clause_list

        def accept(self, visitor):
            if hasattr(visitor, "visitList_value_clause_list"):
                return visitor.visitList_value_clause_list(self)
            else:
                return visitor.visitChildren(self)




    def list_value_clause_list(self):

        localctx = SQLParser.List_value_clause_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_list_value_clause_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 610
            self.list_value_partition()
            self.state = 615
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.COMMA:
                self.state = 611
                self.match(SQLParser.COMMA)
                self.state = 612
                self.list_value_partition()
                self.state = 617
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class List_value_partitionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.List_value_partitionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PARTITION(self):
            return self.getToken(SQLParser.PARTITION, 0)

        def partition_name(self):
            return self.getTypedRuleContext(SQLParser.Partition_nameContext,0)


        def VALUES(self):
            return self.getToken(SQLParser.VALUES, 0)

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def in_value_list(self):
            return self.getTypedRuleContext(SQLParser.In_value_listContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def IN(self):
            return self.getToken(SQLParser.IN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_list_value_partition

        def accept(self, visitor):
            if hasattr(visitor, "visitList_value_partition"):
                return visitor.visitList_value_partition(self)
            else:
                return visitor.visitChildren(self)




    def list_value_partition(self):

        localctx = SQLParser.List_value_partitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_list_value_partition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 618
            self.match(SQLParser.PARTITION)
            self.state = 619
            self.partition_name()
            self.state = 620
            self.match(SQLParser.VALUES)
            self.state = 622
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.IN:
                self.state = 621
                self.match(SQLParser.IN)


            self.state = 624
            self.match(SQLParser.LEFT_PAREN)
            self.state = 625
            self.in_value_list()
            self.state = 626
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Column_partitionsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Column_partitionsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PARTITION(self):
            return self.getToken(SQLParser.PARTITION, 0)

        def BY(self):
            return self.getToken(SQLParser.BY, 0)

        def COLUMN(self):
            return self.getToken(SQLParser.COLUMN, 0)

        def table_elements(self):
            return self.getTypedRuleContext(SQLParser.Table_elementsContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_column_partitions

        def accept(self, visitor):
            if hasattr(visitor, "visitColumn_partitions"):
                return visitor.visitColumn_partitions(self)
            else:
                return visitor.visitChildren(self)




    def column_partitions(self):

        localctx = SQLParser.Column_partitionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_column_partitions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 628
            self.match(SQLParser.PARTITION)
            self.state = 629
            self.match(SQLParser.BY)
            self.state = 630
            self.match(SQLParser.COLUMN)
            self.state = 631
            self.table_elements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Partition_nameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Partition_nameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_partition_name

        def accept(self, visitor):
            if hasattr(visitor, "visitPartition_name"):
                return visitor.visitPartition_name(self)
            else:
                return visitor.visitChildren(self)




    def partition_name(self):

        localctx = SQLParser.Partition_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_partition_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 633
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Drop_table_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Drop_table_statementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DROP(self):
            return self.getToken(SQLParser.DROP, 0)

        def TABLE(self):
            return self.getToken(SQLParser.TABLE, 0)

        def table_name(self):
            return self.getTypedRuleContext(SQLParser.Table_nameContext,0)


        def PURGE(self):
            return self.getToken(SQLParser.PURGE, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_drop_table_statement

        def accept(self, visitor):
            if hasattr(visitor, "visitDrop_table_statement"):
                return visitor.visitDrop_table_statement(self)
            else:
                return visitor.visitChildren(self)




    def drop_table_statement(self):

        localctx = SQLParser.Drop_table_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_drop_table_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            self.match(SQLParser.DROP)
            self.state = 636
            self.match(SQLParser.TABLE)
            self.state = 637
            self.table_name()
            self.state = 639
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.PURGE:
                self.state = 638
                self.match(SQLParser.PURGE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.IdentifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SQLParser.Identifier, 0)

        def nonreserved_keywords(self):
            return self.getTypedRuleContext(SQLParser.Nonreserved_keywordsContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_identifier

        def accept(self, visitor):
            if hasattr(visitor, "visitIdentifier"):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = SQLParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_identifier)
        try:
            self.state = 643
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 641
                self.match(SQLParser.Identifier)
                pass
            elif token in [SQLParser.AVG, SQLParser.BETWEEN, SQLParser.BY, SQLParser.CENTURY, SQLParser.CHARACTER, SQLParser.COLLECT, SQLParser.COALESCE, SQLParser.COLUMN, SQLParser.COUNT, SQLParser.CUBE, SQLParser.DAY, SQLParser.DEC, SQLParser.DECADE, SQLParser.DOW, SQLParser.DOY, SQLParser.DROP, SQLParser.EPOCH, SQLParser.EVERY, SQLParser.EXISTS, SQLParser.EXTERNAL, SQLParser.EXTRACT, SQLParser.FILTER, SQLParser.FIRST, SQLParser.FORMAT, SQLParser.FUSION, SQLParser.GROUPING, SQLParser.HASH, SQLParser.INDEX, SQLParser.INSERT, SQLParser.INTERSECTION, SQLParser.ISODOW, SQLParser.ISOYEAR, SQLParser.LAST, SQLParser.LESS, SQLParser.LIST, SQLParser.LOCATION, SQLParser.MAX, SQLParser.MAXVALUE, SQLParser.MICROSECONDS, SQLParser.MILLENNIUM, SQLParser.MILLISECONDS, SQLParser.MIN, SQLParser.MINUTE, SQLParser.MONTH, SQLParser.NATIONAL, SQLParser.NULLIF, SQLParser.OVERWRITE, SQLParser.PARTITION, SQLParser.PARTITIONS, SQLParser.PRECISION, SQLParser.PURGE, SQLParser.QUARTER, SQLParser.RANGE, SQLParser.REGEXP, SQLParser.RLIKE, SQLParser.ROLLUP, SQLParser.SECOND, SQLParser.SET, SQLParser.SIMILAR, SQLParser.STDDEV_POP, SQLParser.STDDEV_SAMP, SQLParser.SUBPARTITION, SQLParser.SUM, SQLParser.TABLESPACE, SQLParser.THAN, SQLParser.TIMEZONE, SQLParser.TIMEZONE_HOUR, SQLParser.TIMEZONE_MINUTE, SQLParser.TRIM, SQLParser.TO, SQLParser.UNKNOWN, SQLParser.VALUES, SQLParser.VAR_SAMP, SQLParser.VAR_POP, SQLParser.VARYING, SQLParser.WEEK, SQLParser.YEAR, SQLParser.ZONE, SQLParser.BOOLEAN, SQLParser.BOOL, SQLParser.BIT, SQLParser.VARBIT, SQLParser.INT1, SQLParser.INT2, SQLParser.INT4, SQLParser.INT8, SQLParser.TINYINT, SQLParser.SMALLINT, SQLParser.INT, SQLParser.INTEGER, SQLParser.BIGINT, SQLParser.FLOAT4, SQLParser.FLOAT8, SQLParser.REAL, SQLParser.FLOAT, SQLParser.DOUBLE, SQLParser.NUMERIC, SQLParser.DECIMAL, SQLParser.CHAR, SQLParser.VARCHAR, SQLParser.NCHAR, SQLParser.NVARCHAR, SQLParser.DATE, SQLParser.TIME, SQLParser.TIMETZ, SQLParser.TIMESTAMP, SQLParser.TIMESTAMPTZ, SQLParser.TEXT, SQLParser.VARBINARY, SQLParser.BLOB, SQLParser.BYTEA, SQLParser.INET4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 642
                self.nonreserved_keywords()
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

    class Nonreserved_keywordsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Nonreserved_keywordsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def AVG(self):
            return self.getToken(SQLParser.AVG, 0)

        def BETWEEN(self):
            return self.getToken(SQLParser.BETWEEN, 0)

        def BY(self):
            return self.getToken(SQLParser.BY, 0)

        def CENTURY(self):
            return self.getToken(SQLParser.CENTURY, 0)

        def CHARACTER(self):
            return self.getToken(SQLParser.CHARACTER, 0)

        def COALESCE(self):
            return self.getToken(SQLParser.COALESCE, 0)

        def COLLECT(self):
            return self.getToken(SQLParser.COLLECT, 0)

        def COLUMN(self):
            return self.getToken(SQLParser.COLUMN, 0)

        def COUNT(self):
            return self.getToken(SQLParser.COUNT, 0)

        def CUBE(self):
            return self.getToken(SQLParser.CUBE, 0)

        def DAY(self):
            return self.getToken(SQLParser.DAY, 0)

        def DEC(self):
            return self.getToken(SQLParser.DEC, 0)

        def DECADE(self):
            return self.getToken(SQLParser.DECADE, 0)

        def DOW(self):
            return self.getToken(SQLParser.DOW, 0)

        def DOY(self):
            return self.getToken(SQLParser.DOY, 0)

        def DROP(self):
            return self.getToken(SQLParser.DROP, 0)

        def EPOCH(self):
            return self.getToken(SQLParser.EPOCH, 0)

        def EVERY(self):
            return self.getToken(SQLParser.EVERY, 0)

        def EXISTS(self):
            return self.getToken(SQLParser.EXISTS, 0)

        def EXTERNAL(self):
            return self.getToken(SQLParser.EXTERNAL, 0)

        def EXTRACT(self):
            return self.getToken(SQLParser.EXTRACT, 0)

        def FILTER(self):
            return self.getToken(SQLParser.FILTER, 0)

        def FIRST(self):
            return self.getToken(SQLParser.FIRST, 0)

        def FORMAT(self):
            return self.getToken(SQLParser.FORMAT, 0)

        def FUSION(self):
            return self.getToken(SQLParser.FUSION, 0)

        def GROUPING(self):
            return self.getToken(SQLParser.GROUPING, 0)

        def HASH(self):
            return self.getToken(SQLParser.HASH, 0)

        def INDEX(self):
            return self.getToken(SQLParser.INDEX, 0)

        def INSERT(self):
            return self.getToken(SQLParser.INSERT, 0)

        def INTERSECTION(self):
            return self.getToken(SQLParser.INTERSECTION, 0)

        def ISODOW(self):
            return self.getToken(SQLParser.ISODOW, 0)

        def ISOYEAR(self):
            return self.getToken(SQLParser.ISOYEAR, 0)

        def LAST(self):
            return self.getToken(SQLParser.LAST, 0)

        def LESS(self):
            return self.getToken(SQLParser.LESS, 0)

        def LIST(self):
            return self.getToken(SQLParser.LIST, 0)

        def LOCATION(self):
            return self.getToken(SQLParser.LOCATION, 0)

        def MAX(self):
            return self.getToken(SQLParser.MAX, 0)

        def MAXVALUE(self):
            return self.getToken(SQLParser.MAXVALUE, 0)

        def MICROSECONDS(self):
            return self.getToken(SQLParser.MICROSECONDS, 0)

        def MILLENNIUM(self):
            return self.getToken(SQLParser.MILLENNIUM, 0)

        def MILLISECONDS(self):
            return self.getToken(SQLParser.MILLISECONDS, 0)

        def MIN(self):
            return self.getToken(SQLParser.MIN, 0)

        def MINUTE(self):
            return self.getToken(SQLParser.MINUTE, 0)

        def MONTH(self):
            return self.getToken(SQLParser.MONTH, 0)

        def NATIONAL(self):
            return self.getToken(SQLParser.NATIONAL, 0)

        def NULLIF(self):
            return self.getToken(SQLParser.NULLIF, 0)

        def OVERWRITE(self):
            return self.getToken(SQLParser.OVERWRITE, 0)

        def PARTITION(self):
            return self.getToken(SQLParser.PARTITION, 0)

        def PARTITIONS(self):
            return self.getToken(SQLParser.PARTITIONS, 0)

        def PRECISION(self):
            return self.getToken(SQLParser.PRECISION, 0)

        def PURGE(self):
            return self.getToken(SQLParser.PURGE, 0)

        def QUARTER(self):
            return self.getToken(SQLParser.QUARTER, 0)

        def RANGE(self):
            return self.getToken(SQLParser.RANGE, 0)

        def REGEXP(self):
            return self.getToken(SQLParser.REGEXP, 0)

        def RLIKE(self):
            return self.getToken(SQLParser.RLIKE, 0)

        def ROLLUP(self):
            return self.getToken(SQLParser.ROLLUP, 0)

        def SECOND(self):
            return self.getToken(SQLParser.SECOND, 0)

        def SET(self):
            return self.getToken(SQLParser.SET, 0)

        def SIMILAR(self):
            return self.getToken(SQLParser.SIMILAR, 0)

        def STDDEV_POP(self):
            return self.getToken(SQLParser.STDDEV_POP, 0)

        def STDDEV_SAMP(self):
            return self.getToken(SQLParser.STDDEV_SAMP, 0)

        def SUBPARTITION(self):
            return self.getToken(SQLParser.SUBPARTITION, 0)

        def SUM(self):
            return self.getToken(SQLParser.SUM, 0)

        def TABLESPACE(self):
            return self.getToken(SQLParser.TABLESPACE, 0)

        def THAN(self):
            return self.getToken(SQLParser.THAN, 0)

        def TIMEZONE(self):
            return self.getToken(SQLParser.TIMEZONE, 0)

        def TIMEZONE_HOUR(self):
            return self.getToken(SQLParser.TIMEZONE_HOUR, 0)

        def TIMEZONE_MINUTE(self):
            return self.getToken(SQLParser.TIMEZONE_MINUTE, 0)

        def TRIM(self):
            return self.getToken(SQLParser.TRIM, 0)

        def TO(self):
            return self.getToken(SQLParser.TO, 0)

        def UNKNOWN(self):
            return self.getToken(SQLParser.UNKNOWN, 0)

        def VALUES(self):
            return self.getToken(SQLParser.VALUES, 0)

        def VAR_POP(self):
            return self.getToken(SQLParser.VAR_POP, 0)

        def VAR_SAMP(self):
            return self.getToken(SQLParser.VAR_SAMP, 0)

        def VARYING(self):
            return self.getToken(SQLParser.VARYING, 0)

        def WEEK(self):
            return self.getToken(SQLParser.WEEK, 0)

        def YEAR(self):
            return self.getToken(SQLParser.YEAR, 0)

        def ZONE(self):
            return self.getToken(SQLParser.ZONE, 0)

        def BIGINT(self):
            return self.getToken(SQLParser.BIGINT, 0)

        def BIT(self):
            return self.getToken(SQLParser.BIT, 0)

        def BLOB(self):
            return self.getToken(SQLParser.BLOB, 0)

        def BOOL(self):
            return self.getToken(SQLParser.BOOL, 0)

        def BOOLEAN(self):
            return self.getToken(SQLParser.BOOLEAN, 0)

        def BYTEA(self):
            return self.getToken(SQLParser.BYTEA, 0)

        def CHAR(self):
            return self.getToken(SQLParser.CHAR, 0)

        def DATE(self):
            return self.getToken(SQLParser.DATE, 0)

        def DECIMAL(self):
            return self.getToken(SQLParser.DECIMAL, 0)

        def DOUBLE(self):
            return self.getToken(SQLParser.DOUBLE, 0)

        def FLOAT(self):
            return self.getToken(SQLParser.FLOAT, 0)

        def FLOAT4(self):
            return self.getToken(SQLParser.FLOAT4, 0)

        def FLOAT8(self):
            return self.getToken(SQLParser.FLOAT8, 0)

        def INET4(self):
            return self.getToken(SQLParser.INET4, 0)

        def INT(self):
            return self.getToken(SQLParser.INT, 0)

        def INT1(self):
            return self.getToken(SQLParser.INT1, 0)

        def INT2(self):
            return self.getToken(SQLParser.INT2, 0)

        def INT4(self):
            return self.getToken(SQLParser.INT4, 0)

        def INT8(self):
            return self.getToken(SQLParser.INT8, 0)

        def INTEGER(self):
            return self.getToken(SQLParser.INTEGER, 0)

        def NCHAR(self):
            return self.getToken(SQLParser.NCHAR, 0)

        def NUMERIC(self):
            return self.getToken(SQLParser.NUMERIC, 0)

        def NVARCHAR(self):
            return self.getToken(SQLParser.NVARCHAR, 0)

        def REAL(self):
            return self.getToken(SQLParser.REAL, 0)

        def SMALLINT(self):
            return self.getToken(SQLParser.SMALLINT, 0)

        def TEXT(self):
            return self.getToken(SQLParser.TEXT, 0)

        def TIME(self):
            return self.getToken(SQLParser.TIME, 0)

        def TIMESTAMP(self):
            return self.getToken(SQLParser.TIMESTAMP, 0)

        def TIMESTAMPTZ(self):
            return self.getToken(SQLParser.TIMESTAMPTZ, 0)

        def TIMETZ(self):
            return self.getToken(SQLParser.TIMETZ, 0)

        def TINYINT(self):
            return self.getToken(SQLParser.TINYINT, 0)

        def VARBINARY(self):
            return self.getToken(SQLParser.VARBINARY, 0)

        def VARBIT(self):
            return self.getToken(SQLParser.VARBIT, 0)

        def VARCHAR(self):
            return self.getToken(SQLParser.VARCHAR, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_nonreserved_keywords

        def accept(self, visitor):
            if hasattr(visitor, "visitNonreserved_keywords"):
                return visitor.visitNonreserved_keywords(self)
            else:
                return visitor.visitChildren(self)




    def nonreserved_keywords(self):

        localctx = SQLParser.Nonreserved_keywordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_nonreserved_keywords)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 645
            _la = self._input.LA(1)
            if not(((((_la - 54)) & ~0x3f) == 0 and ((1 << (_la - 54)) & ((1 << (SQLParser.AVG - 54)) | (1 << (SQLParser.BETWEEN - 54)) | (1 << (SQLParser.BY - 54)) | (1 << (SQLParser.CENTURY - 54)) | (1 << (SQLParser.CHARACTER - 54)) | (1 << (SQLParser.COLLECT - 54)) | (1 << (SQLParser.COALESCE - 54)) | (1 << (SQLParser.COLUMN - 54)) | (1 << (SQLParser.COUNT - 54)) | (1 << (SQLParser.CUBE - 54)) | (1 << (SQLParser.DAY - 54)) | (1 << (SQLParser.DEC - 54)) | (1 << (SQLParser.DECADE - 54)) | (1 << (SQLParser.DOW - 54)) | (1 << (SQLParser.DOY - 54)) | (1 << (SQLParser.DROP - 54)) | (1 << (SQLParser.EPOCH - 54)) | (1 << (SQLParser.EVERY - 54)) | (1 << (SQLParser.EXISTS - 54)) | (1 << (SQLParser.EXTERNAL - 54)) | (1 << (SQLParser.EXTRACT - 54)) | (1 << (SQLParser.FILTER - 54)) | (1 << (SQLParser.FIRST - 54)) | (1 << (SQLParser.FORMAT - 54)) | (1 << (SQLParser.FUSION - 54)) | (1 << (SQLParser.GROUPING - 54)) | (1 << (SQLParser.HASH - 54)) | (1 << (SQLParser.INDEX - 54)) | (1 << (SQLParser.INSERT - 54)) | (1 << (SQLParser.INTERSECTION - 54)) | (1 << (SQLParser.ISODOW - 54)) | (1 << (SQLParser.ISOYEAR - 54)) | (1 << (SQLParser.LAST - 54)) | (1 << (SQLParser.LESS - 54)) | (1 << (SQLParser.LIST - 54)) | (1 << (SQLParser.LOCATION - 54)) | (1 << (SQLParser.MAX - 54)) | (1 << (SQLParser.MAXVALUE - 54)) | (1 << (SQLParser.MICROSECONDS - 54)) | (1 << (SQLParser.MILLENNIUM - 54)) | (1 << (SQLParser.MILLISECONDS - 54)) | (1 << (SQLParser.MIN - 54)) | (1 << (SQLParser.MINUTE - 54)) | (1 << (SQLParser.MONTH - 54)) | (1 << (SQLParser.NATIONAL - 54)) | (1 << (SQLParser.NULLIF - 54)) | (1 << (SQLParser.OVERWRITE - 54)) | (1 << (SQLParser.PARTITION - 54)) | (1 << (SQLParser.PARTITIONS - 54)) | (1 << (SQLParser.PRECISION - 54)) | (1 << (SQLParser.PURGE - 54)) | (1 << (SQLParser.QUARTER - 54)) | (1 << (SQLParser.RANGE - 54)) | (1 << (SQLParser.REGEXP - 54)) | (1 << (SQLParser.RLIKE - 54)) | (1 << (SQLParser.ROLLUP - 54)) | (1 << (SQLParser.SECOND - 54)) | (1 << (SQLParser.SET - 54)) | (1 << (SQLParser.SIMILAR - 54)) | (1 << (SQLParser.STDDEV_POP - 54)) | (1 << (SQLParser.STDDEV_SAMP - 54)) | (1 << (SQLParser.SUBPARTITION - 54)) | (1 << (SQLParser.SUM - 54)))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (SQLParser.TABLESPACE - 118)) | (1 << (SQLParser.THAN - 118)) | (1 << (SQLParser.TIMEZONE - 118)) | (1 << (SQLParser.TIMEZONE_HOUR - 118)) | (1 << (SQLParser.TIMEZONE_MINUTE - 118)) | (1 << (SQLParser.TRIM - 118)) | (1 << (SQLParser.TO - 118)) | (1 << (SQLParser.UNKNOWN - 118)) | (1 << (SQLParser.VALUES - 118)) | (1 << (SQLParser.VAR_SAMP - 118)) | (1 << (SQLParser.VAR_POP - 118)) | (1 << (SQLParser.VARYING - 118)) | (1 << (SQLParser.WEEK - 118)) | (1 << (SQLParser.YEAR - 118)) | (1 << (SQLParser.ZONE - 118)) | (1 << (SQLParser.BOOLEAN - 118)) | (1 << (SQLParser.BOOL - 118)) | (1 << (SQLParser.BIT - 118)) | (1 << (SQLParser.VARBIT - 118)) | (1 << (SQLParser.INT1 - 118)) | (1 << (SQLParser.INT2 - 118)) | (1 << (SQLParser.INT4 - 118)) | (1 << (SQLParser.INT8 - 118)) | (1 << (SQLParser.TINYINT - 118)) | (1 << (SQLParser.SMALLINT - 118)) | (1 << (SQLParser.INT - 118)) | (1 << (SQLParser.INTEGER - 118)) | (1 << (SQLParser.BIGINT - 118)) | (1 << (SQLParser.FLOAT4 - 118)) | (1 << (SQLParser.FLOAT8 - 118)) | (1 << (SQLParser.REAL - 118)) | (1 << (SQLParser.FLOAT - 118)) | (1 << (SQLParser.DOUBLE - 118)) | (1 << (SQLParser.NUMERIC - 118)) | (1 << (SQLParser.DECIMAL - 118)) | (1 << (SQLParser.CHAR - 118)) | (1 << (SQLParser.VARCHAR - 118)) | (1 << (SQLParser.NCHAR - 118)) | (1 << (SQLParser.NVARCHAR - 118)) | (1 << (SQLParser.DATE - 118)) | (1 << (SQLParser.TIME - 118)) | (1 << (SQLParser.TIMETZ - 118)) | (1 << (SQLParser.TIMESTAMP - 118)) | (1 << (SQLParser.TIMESTAMPTZ - 118)) | (1 << (SQLParser.TEXT - 118)) | (1 << (SQLParser.VARBINARY - 118)) | (1 << (SQLParser.BLOB - 118)) | (1 << (SQLParser.BYTEA - 118)) | (1 << (SQLParser.INET4 - 118)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Unsigned_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Unsigned_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def unsigned_numeric_literal(self):
            return self.getTypedRuleContext(SQLParser.Unsigned_numeric_literalContext,0)


        def general_literal(self):
            return self.getTypedRuleContext(SQLParser.General_literalContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_unsigned_literal

        def accept(self, visitor):
            if hasattr(visitor, "visitUnsigned_literal"):
                return visitor.visitUnsigned_literal(self)
            else:
                return visitor.visitChildren(self)




    def unsigned_literal(self):

        localctx = SQLParser.Unsigned_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_unsigned_literal)
        try:
            self.state = 649
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.NUMBER, SQLParser.REAL_NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 647
                self.unsigned_numeric_literal()
                pass
            elif token in [SQLParser.FALSE, SQLParser.TRUE, SQLParser.UNKNOWN, SQLParser.DATE, SQLParser.TIME, SQLParser.TIMESTAMP, SQLParser.Character_String_Literal]:
                self.enterOuterAlt(localctx, 2)
                self.state = 648
                self.general_literal()
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

    class General_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.General_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Character_String_Literal(self):
            return self.getToken(SQLParser.Character_String_Literal, 0)

        def datetime_literal(self):
            return self.getTypedRuleContext(SQLParser.Datetime_literalContext,0)


        def boolean_literal(self):
            return self.getTypedRuleContext(SQLParser.Boolean_literalContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_general_literal

        def accept(self, visitor):
            if hasattr(visitor, "visitGeneral_literal"):
                return visitor.visitGeneral_literal(self)
            else:
                return visitor.visitChildren(self)




    def general_literal(self):

        localctx = SQLParser.General_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_general_literal)
        try:
            self.state = 654
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.Character_String_Literal]:
                self.enterOuterAlt(localctx, 1)
                self.state = 651
                self.match(SQLParser.Character_String_Literal)
                pass
            elif token in [SQLParser.DATE, SQLParser.TIME, SQLParser.TIMESTAMP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 652
                self.datetime_literal()
                pass
            elif token in [SQLParser.FALSE, SQLParser.TRUE, SQLParser.UNKNOWN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 653
                self.boolean_literal()
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

    class Datetime_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Datetime_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def timestamp_literal(self):
            return self.getTypedRuleContext(SQLParser.Timestamp_literalContext,0)


        def time_literal(self):
            return self.getTypedRuleContext(SQLParser.Time_literalContext,0)


        def date_literal(self):
            return self.getTypedRuleContext(SQLParser.Date_literalContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_datetime_literal

        def accept(self, visitor):
            if hasattr(visitor, "visitDatetime_literal"):
                return visitor.visitDatetime_literal(self)
            else:
                return visitor.visitChildren(self)




    def datetime_literal(self):

        localctx = SQLParser.Datetime_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_datetime_literal)
        try:
            self.state = 659
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.TIMESTAMP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 656
                self.timestamp_literal()
                pass
            elif token in [SQLParser.TIME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 657
                self.time_literal()
                pass
            elif token in [SQLParser.DATE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 658
                self.date_literal()
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

    class Time_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Time_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.time_string = None # Token

        def TIME(self):
            return self.getToken(SQLParser.TIME, 0)

        def Character_String_Literal(self):
            return self.getToken(SQLParser.Character_String_Literal, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_time_literal

        def accept(self, visitor):
            if hasattr(visitor, "visitTime_literal"):
                return visitor.visitTime_literal(self)
            else:
                return visitor.visitChildren(self)




    def time_literal(self):

        localctx = SQLParser.Time_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_time_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 661
            self.match(SQLParser.TIME)
            self.state = 662
            localctx.time_string = self.match(SQLParser.Character_String_Literal)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Timestamp_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Timestamp_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.timestamp_string = None # Token

        def TIMESTAMP(self):
            return self.getToken(SQLParser.TIMESTAMP, 0)

        def Character_String_Literal(self):
            return self.getToken(SQLParser.Character_String_Literal, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_timestamp_literal

        def accept(self, visitor):
            if hasattr(visitor, "visitTimestamp_literal"):
                return visitor.visitTimestamp_literal(self)
            else:
                return visitor.visitChildren(self)




    def timestamp_literal(self):

        localctx = SQLParser.Timestamp_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_timestamp_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 664
            self.match(SQLParser.TIMESTAMP)
            self.state = 665
            localctx.timestamp_string = self.match(SQLParser.Character_String_Literal)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Date_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Date_literalContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.date_string = None # Token

        def DATE(self):
            return self.getToken(SQLParser.DATE, 0)

        def Character_String_Literal(self):
            return self.getToken(SQLParser.Character_String_Literal, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_date_literal

        def accept(self, visitor):
            if hasattr(visitor, "visitDate_literal"):
                return visitor.visitDate_literal(self)
            else:
                return visitor.visitChildren(self)




    def date_literal(self):

        localctx = SQLParser.Date_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_date_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 667
            self.match(SQLParser.DATE)
            self.state = 668
            localctx.date_string = self.match(SQLParser.Character_String_Literal)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Boolean_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Boolean_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(SQLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(SQLParser.FALSE, 0)

        def UNKNOWN(self):
            return self.getToken(SQLParser.UNKNOWN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_boolean_literal

        def accept(self, visitor):
            if hasattr(visitor, "visitBoolean_literal"):
                return visitor.visitBoolean_literal(self)
            else:
                return visitor.visitChildren(self)




    def boolean_literal(self):

        localctx = SQLParser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 670
            _la = self._input.LA(1)
            if not(_la==SQLParser.FALSE or _la==SQLParser.TRUE or _la==SQLParser.UNKNOWN):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Data_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Data_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def predefined_type(self):
            return self.getTypedRuleContext(SQLParser.Predefined_typeContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_data_type

        def accept(self, visitor):
            if hasattr(visitor, "visitData_type"):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = SQLParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_data_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 672
            self.predefined_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Predefined_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Predefined_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def character_string_type(self):
            return self.getTypedRuleContext(SQLParser.Character_string_typeContext,0)


        def national_character_string_type(self):
            return self.getTypedRuleContext(SQLParser.National_character_string_typeContext,0)


        def binary_large_object_string_type(self):
            return self.getTypedRuleContext(SQLParser.Binary_large_object_string_typeContext,0)


        def numeric_type(self):
            return self.getTypedRuleContext(SQLParser.Numeric_typeContext,0)


        def boolean_type(self):
            return self.getTypedRuleContext(SQLParser.Boolean_typeContext,0)


        def datetime_type(self):
            return self.getTypedRuleContext(SQLParser.Datetime_typeContext,0)


        def bit_type(self):
            return self.getTypedRuleContext(SQLParser.Bit_typeContext,0)


        def binary_type(self):
            return self.getTypedRuleContext(SQLParser.Binary_typeContext,0)


        def network_type(self):
            return self.getTypedRuleContext(SQLParser.Network_typeContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_predefined_type

        def accept(self, visitor):
            if hasattr(visitor, "visitPredefined_type"):
                return visitor.visitPredefined_type(self)
            else:
                return visitor.visitChildren(self)




    def predefined_type(self):

        localctx = SQLParser.Predefined_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_predefined_type)
        try:
            self.state = 683
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.CHARACTER, SQLParser.CHAR, SQLParser.VARCHAR, SQLParser.TEXT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 674
                self.character_string_type()
                pass
            elif token in [SQLParser.NATIONAL, SQLParser.NCHAR, SQLParser.NVARCHAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 675
                self.national_character_string_type()
                pass
            elif token in [SQLParser.BLOB, SQLParser.BYTEA]:
                self.enterOuterAlt(localctx, 3)
                self.state = 676
                self.binary_large_object_string_type()
                pass
            elif token in [SQLParser.DEC, SQLParser.INT1, SQLParser.INT2, SQLParser.INT4, SQLParser.INT8, SQLParser.TINYINT, SQLParser.SMALLINT, SQLParser.INT, SQLParser.INTEGER, SQLParser.BIGINT, SQLParser.FLOAT4, SQLParser.FLOAT8, SQLParser.REAL, SQLParser.FLOAT, SQLParser.DOUBLE, SQLParser.NUMERIC, SQLParser.DECIMAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 677
                self.numeric_type()
                pass
            elif token in [SQLParser.BOOLEAN, SQLParser.BOOL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 678
                self.boolean_type()
                pass
            elif token in [SQLParser.DATE, SQLParser.TIME, SQLParser.TIMETZ, SQLParser.TIMESTAMP, SQLParser.TIMESTAMPTZ]:
                self.enterOuterAlt(localctx, 6)
                self.state = 679
                self.datetime_type()
                pass
            elif token in [SQLParser.BIT, SQLParser.VARBIT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 680
                self.bit_type()
                pass
            elif token in [SQLParser.BINARY, SQLParser.VARBINARY]:
                self.enterOuterAlt(localctx, 8)
                self.state = 681
                self.binary_type()
                pass
            elif token in [SQLParser.INET4]:
                self.enterOuterAlt(localctx, 9)
                self.state = 682
                self.network_type()
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

    class Network_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Network_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INET4(self):
            return self.getToken(SQLParser.INET4, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_network_type

        def accept(self, visitor):
            if hasattr(visitor, "visitNetwork_type"):
                return visitor.visitNetwork_type(self)
            else:
                return visitor.visitChildren(self)




    def network_type(self):

        localctx = SQLParser.Network_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_network_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 685
            self.match(SQLParser.INET4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Character_string_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Character_string_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CHARACTER(self):
            return self.getToken(SQLParser.CHARACTER, 0)

        def type_length(self):
            return self.getTypedRuleContext(SQLParser.Type_lengthContext,0)


        def CHAR(self):
            return self.getToken(SQLParser.CHAR, 0)

        def VARYING(self):
            return self.getToken(SQLParser.VARYING, 0)

        def VARCHAR(self):
            return self.getToken(SQLParser.VARCHAR, 0)

        def TEXT(self):
            return self.getToken(SQLParser.TEXT, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_character_string_type

        def accept(self, visitor):
            if hasattr(visitor, "visitCharacter_string_type"):
                return visitor.visitCharacter_string_type(self)
            else:
                return visitor.visitChildren(self)




    def character_string_type(self):

        localctx = SQLParser.Character_string_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_character_string_type)
        self._la = 0 # Token type
        try:
            self.state = 710
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 687
                self.match(SQLParser.CHARACTER)
                self.state = 689
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 688
                    self.type_length()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 691
                self.match(SQLParser.CHAR)
                self.state = 693
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 692
                    self.type_length()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 695
                self.match(SQLParser.CHARACTER)
                self.state = 696
                self.match(SQLParser.VARYING)
                self.state = 698
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 697
                    self.type_length()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 700
                self.match(SQLParser.CHAR)
                self.state = 701
                self.match(SQLParser.VARYING)
                self.state = 703
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 702
                    self.type_length()


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 705
                self.match(SQLParser.VARCHAR)
                self.state = 707
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 706
                    self.type_length()


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 709
                self.match(SQLParser.TEXT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_lengthContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Type_lengthContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def NUMBER(self):
            return self.getToken(SQLParser.NUMBER, 0)

        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_type_length

        def accept(self, visitor):
            if hasattr(visitor, "visitType_length"):
                return visitor.visitType_length(self)
            else:
                return visitor.visitChildren(self)




    def type_length(self):

        localctx = SQLParser.Type_lengthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_type_length)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 712
            self.match(SQLParser.LEFT_PAREN)
            self.state = 713
            self.match(SQLParser.NUMBER)
            self.state = 714
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class National_character_string_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.National_character_string_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NATIONAL(self):
            return self.getToken(SQLParser.NATIONAL, 0)

        def CHARACTER(self):
            return self.getToken(SQLParser.CHARACTER, 0)

        def type_length(self):
            return self.getTypedRuleContext(SQLParser.Type_lengthContext,0)


        def CHAR(self):
            return self.getToken(SQLParser.CHAR, 0)

        def NCHAR(self):
            return self.getToken(SQLParser.NCHAR, 0)

        def VARYING(self):
            return self.getToken(SQLParser.VARYING, 0)

        def NVARCHAR(self):
            return self.getToken(SQLParser.NVARCHAR, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_national_character_string_type

        def accept(self, visitor):
            if hasattr(visitor, "visitNational_character_string_type"):
                return visitor.visitNational_character_string_type(self)
            else:
                return visitor.visitChildren(self)




    def national_character_string_type(self):

        localctx = SQLParser.National_character_string_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_national_character_string_type)
        self._la = 0 # Token type
        try:
            self.state = 751
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 716
                self.match(SQLParser.NATIONAL)
                self.state = 717
                self.match(SQLParser.CHARACTER)
                self.state = 719
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 718
                    self.type_length()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 721
                self.match(SQLParser.NATIONAL)
                self.state = 722
                self.match(SQLParser.CHAR)
                self.state = 724
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 723
                    self.type_length()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 726
                self.match(SQLParser.NCHAR)
                self.state = 728
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 727
                    self.type_length()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 730
                self.match(SQLParser.NATIONAL)
                self.state = 731
                self.match(SQLParser.CHARACTER)
                self.state = 732
                self.match(SQLParser.VARYING)
                self.state = 734
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 733
                    self.type_length()


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 736
                self.match(SQLParser.NATIONAL)
                self.state = 737
                self.match(SQLParser.CHAR)
                self.state = 738
                self.match(SQLParser.VARYING)
                self.state = 740
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 739
                    self.type_length()


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 742
                self.match(SQLParser.NCHAR)
                self.state = 743
                self.match(SQLParser.VARYING)
                self.state = 745
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 744
                    self.type_length()


                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 747
                self.match(SQLParser.NVARCHAR)
                self.state = 749
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 748
                    self.type_length()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Binary_large_object_string_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Binary_large_object_string_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BLOB(self):
            return self.getToken(SQLParser.BLOB, 0)

        def type_length(self):
            return self.getTypedRuleContext(SQLParser.Type_lengthContext,0)


        def BYTEA(self):
            return self.getToken(SQLParser.BYTEA, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_binary_large_object_string_type

        def accept(self, visitor):
            if hasattr(visitor, "visitBinary_large_object_string_type"):
                return visitor.visitBinary_large_object_string_type(self)
            else:
                return visitor.visitChildren(self)




    def binary_large_object_string_type(self):

        localctx = SQLParser.Binary_large_object_string_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_binary_large_object_string_type)
        self._la = 0 # Token type
        try:
            self.state = 761
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.BLOB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 753
                self.match(SQLParser.BLOB)
                self.state = 755
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 754
                    self.type_length()


                pass
            elif token in [SQLParser.BYTEA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 757
                self.match(SQLParser.BYTEA)
                self.state = 759
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 758
                    self.type_length()


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

    class Numeric_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Numeric_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def exact_numeric_type(self):
            return self.getTypedRuleContext(SQLParser.Exact_numeric_typeContext,0)


        def approximate_numeric_type(self):
            return self.getTypedRuleContext(SQLParser.Approximate_numeric_typeContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_numeric_type

        def accept(self, visitor):
            if hasattr(visitor, "visitNumeric_type"):
                return visitor.visitNumeric_type(self)
            else:
                return visitor.visitChildren(self)




    def numeric_type(self):

        localctx = SQLParser.Numeric_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_numeric_type)
        try:
            self.state = 765
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.DEC, SQLParser.INT1, SQLParser.INT2, SQLParser.INT4, SQLParser.INT8, SQLParser.TINYINT, SQLParser.SMALLINT, SQLParser.INT, SQLParser.INTEGER, SQLParser.BIGINT, SQLParser.NUMERIC, SQLParser.DECIMAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 763
                self.exact_numeric_type()
                pass
            elif token in [SQLParser.FLOAT4, SQLParser.FLOAT8, SQLParser.REAL, SQLParser.FLOAT, SQLParser.DOUBLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 764
                self.approximate_numeric_type()
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

    class Exact_numeric_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Exact_numeric_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NUMERIC(self):
            return self.getToken(SQLParser.NUMERIC, 0)

        def precision_param(self):
            return self.getTypedRuleContext(SQLParser.Precision_paramContext,0)


        def DECIMAL(self):
            return self.getToken(SQLParser.DECIMAL, 0)

        def DEC(self):
            return self.getToken(SQLParser.DEC, 0)

        def INT1(self):
            return self.getToken(SQLParser.INT1, 0)

        def TINYINT(self):
            return self.getToken(SQLParser.TINYINT, 0)

        def INT2(self):
            return self.getToken(SQLParser.INT2, 0)

        def SMALLINT(self):
            return self.getToken(SQLParser.SMALLINT, 0)

        def INT4(self):
            return self.getToken(SQLParser.INT4, 0)

        def INT(self):
            return self.getToken(SQLParser.INT, 0)

        def INTEGER(self):
            return self.getToken(SQLParser.INTEGER, 0)

        def INT8(self):
            return self.getToken(SQLParser.INT8, 0)

        def BIGINT(self):
            return self.getToken(SQLParser.BIGINT, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_exact_numeric_type

        def accept(self, visitor):
            if hasattr(visitor, "visitExact_numeric_type"):
                return visitor.visitExact_numeric_type(self)
            else:
                return visitor.visitChildren(self)




    def exact_numeric_type(self):

        localctx = SQLParser.Exact_numeric_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_exact_numeric_type)
        self._la = 0 # Token type
        try:
            self.state = 788
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.NUMERIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 767
                self.match(SQLParser.NUMERIC)
                self.state = 769
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 768
                    self.precision_param()


                pass
            elif token in [SQLParser.DECIMAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 771
                self.match(SQLParser.DECIMAL)
                self.state = 773
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 772
                    self.precision_param()


                pass
            elif token in [SQLParser.DEC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 775
                self.match(SQLParser.DEC)
                self.state = 777
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 776
                    self.precision_param()


                pass
            elif token in [SQLParser.INT1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 779
                self.match(SQLParser.INT1)
                pass
            elif token in [SQLParser.TINYINT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 780
                self.match(SQLParser.TINYINT)
                pass
            elif token in [SQLParser.INT2]:
                self.enterOuterAlt(localctx, 6)
                self.state = 781
                self.match(SQLParser.INT2)
                pass
            elif token in [SQLParser.SMALLINT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 782
                self.match(SQLParser.SMALLINT)
                pass
            elif token in [SQLParser.INT4]:
                self.enterOuterAlt(localctx, 8)
                self.state = 783
                self.match(SQLParser.INT4)
                pass
            elif token in [SQLParser.INT]:
                self.enterOuterAlt(localctx, 9)
                self.state = 784
                self.match(SQLParser.INT)
                pass
            elif token in [SQLParser.INTEGER]:
                self.enterOuterAlt(localctx, 10)
                self.state = 785
                self.match(SQLParser.INTEGER)
                pass
            elif token in [SQLParser.INT8]:
                self.enterOuterAlt(localctx, 11)
                self.state = 786
                self.match(SQLParser.INT8)
                pass
            elif token in [SQLParser.BIGINT]:
                self.enterOuterAlt(localctx, 12)
                self.state = 787
                self.match(SQLParser.BIGINT)
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

    class Approximate_numeric_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Approximate_numeric_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(SQLParser.FLOAT, 0)

        def precision_param(self):
            return self.getTypedRuleContext(SQLParser.Precision_paramContext,0)


        def FLOAT4(self):
            return self.getToken(SQLParser.FLOAT4, 0)

        def REAL(self):
            return self.getToken(SQLParser.REAL, 0)

        def FLOAT8(self):
            return self.getToken(SQLParser.FLOAT8, 0)

        def DOUBLE(self):
            return self.getToken(SQLParser.DOUBLE, 0)

        def PRECISION(self):
            return self.getToken(SQLParser.PRECISION, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_approximate_numeric_type

        def accept(self, visitor):
            if hasattr(visitor, "visitApproximate_numeric_type"):
                return visitor.visitApproximate_numeric_type(self)
            else:
                return visitor.visitChildren(self)




    def approximate_numeric_type(self):

        localctx = SQLParser.Approximate_numeric_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_approximate_numeric_type)
        self._la = 0 # Token type
        try:
            self.state = 800
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 790
                self.match(SQLParser.FLOAT)
                self.state = 792
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 791
                    self.precision_param()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 794
                self.match(SQLParser.FLOAT4)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 795
                self.match(SQLParser.REAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 796
                self.match(SQLParser.FLOAT8)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 797
                self.match(SQLParser.DOUBLE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 798
                self.match(SQLParser.DOUBLE)
                self.state = 799
                self.match(SQLParser.PRECISION)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Precision_paramContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Precision_paramContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.precision = None # Token
            self.scale = None # Token

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def NUMBER(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.NUMBER)
            else:
                return self.getToken(SQLParser.NUMBER, i)

        def COMMA(self):
            return self.getToken(SQLParser.COMMA, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_precision_param

        def accept(self, visitor):
            if hasattr(visitor, "visitPrecision_param"):
                return visitor.visitPrecision_param(self)
            else:
                return visitor.visitChildren(self)




    def precision_param(self):

        localctx = SQLParser.Precision_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_precision_param)
        try:
            self.state = 810
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 802
                self.match(SQLParser.LEFT_PAREN)
                self.state = 803
                localctx.precision = self.match(SQLParser.NUMBER)
                self.state = 804
                self.match(SQLParser.RIGHT_PAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 805
                self.match(SQLParser.LEFT_PAREN)
                self.state = 806
                localctx.precision = self.match(SQLParser.NUMBER)
                self.state = 807
                self.match(SQLParser.COMMA)
                self.state = 808
                localctx.scale = self.match(SQLParser.NUMBER)
                self.state = 809
                self.match(SQLParser.RIGHT_PAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Boolean_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Boolean_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(SQLParser.BOOLEAN, 0)

        def BOOL(self):
            return self.getToken(SQLParser.BOOL, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_boolean_type

        def accept(self, visitor):
            if hasattr(visitor, "visitBoolean_type"):
                return visitor.visitBoolean_type(self)
            else:
                return visitor.visitChildren(self)




    def boolean_type(self):

        localctx = SQLParser.Boolean_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_boolean_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 812
            _la = self._input.LA(1)
            if not(_la==SQLParser.BOOLEAN or _la==SQLParser.BOOL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Datetime_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Datetime_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DATE(self):
            return self.getToken(SQLParser.DATE, 0)

        def TIME(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.TIME)
            else:
                return self.getToken(SQLParser.TIME, i)

        def WITH(self):
            return self.getToken(SQLParser.WITH, 0)

        def ZONE(self):
            return self.getToken(SQLParser.ZONE, 0)

        def TIMETZ(self):
            return self.getToken(SQLParser.TIMETZ, 0)

        def TIMESTAMP(self):
            return self.getToken(SQLParser.TIMESTAMP, 0)

        def TIMESTAMPTZ(self):
            return self.getToken(SQLParser.TIMESTAMPTZ, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_datetime_type

        def accept(self, visitor):
            if hasattr(visitor, "visitDatetime_type"):
                return visitor.visitDatetime_type(self)
            else:
                return visitor.visitChildren(self)




    def datetime_type(self):

        localctx = SQLParser.Datetime_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_datetime_type)
        try:
            self.state = 827
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 814
                self.match(SQLParser.DATE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 815
                self.match(SQLParser.TIME)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 816
                self.match(SQLParser.TIME)
                self.state = 817
                self.match(SQLParser.WITH)
                self.state = 818
                self.match(SQLParser.TIME)
                self.state = 819
                self.match(SQLParser.ZONE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 820
                self.match(SQLParser.TIMETZ)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 821
                self.match(SQLParser.TIMESTAMP)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 822
                self.match(SQLParser.TIMESTAMP)
                self.state = 823
                self.match(SQLParser.WITH)
                self.state = 824
                self.match(SQLParser.TIME)
                self.state = 825
                self.match(SQLParser.ZONE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 826
                self.match(SQLParser.TIMESTAMPTZ)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Bit_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Bit_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BIT(self):
            return self.getToken(SQLParser.BIT, 0)

        def type_length(self):
            return self.getTypedRuleContext(SQLParser.Type_lengthContext,0)


        def VARBIT(self):
            return self.getToken(SQLParser.VARBIT, 0)

        def VARYING(self):
            return self.getToken(SQLParser.VARYING, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_bit_type

        def accept(self, visitor):
            if hasattr(visitor, "visitBit_type"):
                return visitor.visitBit_type(self)
            else:
                return visitor.visitChildren(self)




    def bit_type(self):

        localctx = SQLParser.Bit_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_bit_type)
        self._la = 0 # Token type
        try:
            self.state = 842
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 829
                self.match(SQLParser.BIT)
                self.state = 831
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 830
                    self.type_length()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 833
                self.match(SQLParser.VARBIT)
                self.state = 835
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 834
                    self.type_length()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 837
                self.match(SQLParser.BIT)
                self.state = 838
                self.match(SQLParser.VARYING)
                self.state = 840
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 839
                    self.type_length()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Binary_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Binary_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BINARY(self):
            return self.getToken(SQLParser.BINARY, 0)

        def type_length(self):
            return self.getTypedRuleContext(SQLParser.Type_lengthContext,0)


        def VARYING(self):
            return self.getToken(SQLParser.VARYING, 0)

        def VARBINARY(self):
            return self.getToken(SQLParser.VARBINARY, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_binary_type

        def accept(self, visitor):
            if hasattr(visitor, "visitBinary_type"):
                return visitor.visitBinary_type(self)
            else:
                return visitor.visitChildren(self)




    def binary_type(self):

        localctx = SQLParser.Binary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_binary_type)
        self._la = 0 # Token type
        try:
            self.state = 857
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 844
                self.match(SQLParser.BINARY)
                self.state = 846
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 845
                    self.type_length()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 848
                self.match(SQLParser.BINARY)
                self.state = 849
                self.match(SQLParser.VARYING)
                self.state = 851
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 850
                    self.type_length()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 853
                self.match(SQLParser.VARBINARY)
                self.state = 855
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 854
                    self.type_length()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Value_expression_primaryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Value_expression_primaryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def parenthesized_value_expression(self):
            return self.getTypedRuleContext(SQLParser.Parenthesized_value_expressionContext,0)


        def nonparenthesized_value_expression_primary(self):
            return self.getTypedRuleContext(SQLParser.Nonparenthesized_value_expression_primaryContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_value_expression_primary

        def accept(self, visitor):
            if hasattr(visitor, "visitValue_expression_primary"):
                return visitor.visitValue_expression_primary(self)
            else:
                return visitor.visitChildren(self)




    def value_expression_primary(self):

        localctx = SQLParser.Value_expression_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_value_expression_primary)
        try:
            self.state = 861
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 859
                self.parenthesized_value_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 860
                self.nonparenthesized_value_expression_primary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Parenthesized_value_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Parenthesized_value_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def value_expression(self):
            return self.getTypedRuleContext(SQLParser.Value_expressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_parenthesized_value_expression

        def accept(self, visitor):
            if hasattr(visitor, "visitParenthesized_value_expression"):
                return visitor.visitParenthesized_value_expression(self)
            else:
                return visitor.visitChildren(self)




    def parenthesized_value_expression(self):

        localctx = SQLParser.Parenthesized_value_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_parenthesized_value_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 863
            self.match(SQLParser.LEFT_PAREN)
            self.state = 864
            self.value_expression()
            self.state = 865
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Nonparenthesized_value_expression_primaryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Nonparenthesized_value_expression_primaryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def unsigned_value_specification(self):
            return self.getTypedRuleContext(SQLParser.Unsigned_value_specificationContext,0)


        def column_reference(self):
            return self.getTypedRuleContext(SQLParser.Column_referenceContext,0)


        def set_function_specification(self):
            return self.getTypedRuleContext(SQLParser.Set_function_specificationContext,0)


        def scalar_subquery(self):
            return self.getTypedRuleContext(SQLParser.Scalar_subqueryContext,0)


        def case_expression(self):
            return self.getTypedRuleContext(SQLParser.Case_expressionContext,0)


        def cast_specification(self):
            return self.getTypedRuleContext(SQLParser.Cast_specificationContext,0)


        def routine_invocation(self):
            return self.getTypedRuleContext(SQLParser.Routine_invocationContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_nonparenthesized_value_expression_primary

        def accept(self, visitor):
            if hasattr(visitor, "visitNonparenthesized_value_expression_primary"):
                return visitor.visitNonparenthesized_value_expression_primary(self)
            else:
                return visitor.visitChildren(self)




    def nonparenthesized_value_expression_primary(self):

        localctx = SQLParser.Nonparenthesized_value_expression_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_nonparenthesized_value_expression_primary)
        try:
            self.state = 874
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 867
                self.unsigned_value_specification()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 868
                self.column_reference()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 869
                self.set_function_specification()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 870
                self.scalar_subquery()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 871
                self.case_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 872
                self.cast_specification()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 873
                self.routine_invocation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Unsigned_value_specificationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Unsigned_value_specificationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def unsigned_literal(self):
            return self.getTypedRuleContext(SQLParser.Unsigned_literalContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_unsigned_value_specification

        def accept(self, visitor):
            if hasattr(visitor, "visitUnsigned_value_specification"):
                return visitor.visitUnsigned_value_specification(self)
            else:
                return visitor.visitChildren(self)




    def unsigned_value_specification(self):

        localctx = SQLParser.Unsigned_value_specificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_unsigned_value_specification)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 876
            self.unsigned_literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Unsigned_numeric_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Unsigned_numeric_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SQLParser.NUMBER, 0)

        def REAL_NUMBER(self):
            return self.getToken(SQLParser.REAL_NUMBER, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_unsigned_numeric_literal

        def accept(self, visitor):
            if hasattr(visitor, "visitUnsigned_numeric_literal"):
                return visitor.visitUnsigned_numeric_literal(self)
            else:
                return visitor.visitChildren(self)




    def unsigned_numeric_literal(self):

        localctx = SQLParser.Unsigned_numeric_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_unsigned_numeric_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 878
            _la = self._input.LA(1)
            if not(_la==SQLParser.NUMBER or _la==SQLParser.REAL_NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Signed_numerical_literalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Signed_numerical_literalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def unsigned_numeric_literal(self):
            return self.getTypedRuleContext(SQLParser.Unsigned_numeric_literalContext,0)


        def sign(self):
            return self.getTypedRuleContext(SQLParser.SignContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_signed_numerical_literal

        def accept(self, visitor):
            if hasattr(visitor, "visitSigned_numerical_literal"):
                return visitor.visitSigned_numerical_literal(self)
            else:
                return visitor.visitChildren(self)




    def signed_numerical_literal(self):

        localctx = SQLParser.Signed_numerical_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_signed_numerical_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 881
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.PLUS or _la==SQLParser.MINUS:
                self.state = 880
                self.sign()


            self.state = 883
            self.unsigned_numeric_literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_function_specificationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Set_function_specificationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def aggregate_function(self):
            return self.getTypedRuleContext(SQLParser.Aggregate_functionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_set_function_specification

        def accept(self, visitor):
            if hasattr(visitor, "visitSet_function_specification"):
                return visitor.visitSet_function_specification(self)
            else:
                return visitor.visitChildren(self)




    def set_function_specification(self):

        localctx = SQLParser.Set_function_specificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_set_function_specification)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 885
            self.aggregate_function()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Aggregate_functionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Aggregate_functionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def COUNT(self):
            return self.getToken(SQLParser.COUNT, 0)

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def MULTIPLY(self):
            return self.getToken(SQLParser.MULTIPLY, 0)

        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def general_set_function(self):
            return self.getTypedRuleContext(SQLParser.General_set_functionContext,0)


        def filter_clause(self):
            return self.getTypedRuleContext(SQLParser.Filter_clauseContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_aggregate_function

        def accept(self, visitor):
            if hasattr(visitor, "visitAggregate_function"):
                return visitor.visitAggregate_function(self)
            else:
                return visitor.visitChildren(self)




    def aggregate_function(self):

        localctx = SQLParser.Aggregate_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_aggregate_function)
        try:
            self.state = 895
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 887
                self.match(SQLParser.COUNT)
                self.state = 888
                self.match(SQLParser.LEFT_PAREN)
                self.state = 889
                self.match(SQLParser.MULTIPLY)
                self.state = 890
                self.match(SQLParser.RIGHT_PAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 891
                self.general_set_function()
                self.state = 893
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
                if la_ == 1:
                    self.state = 892
                    self.filter_clause()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class General_set_functionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.General_set_functionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def set_function_type(self):
            return self.getTypedRuleContext(SQLParser.Set_function_typeContext,0)


        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def value_expression(self):
            return self.getTypedRuleContext(SQLParser.Value_expressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def set_qualifier(self):
            return self.getTypedRuleContext(SQLParser.Set_qualifierContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_general_set_function

        def accept(self, visitor):
            if hasattr(visitor, "visitGeneral_set_function"):
                return visitor.visitGeneral_set_function(self)
            else:
                return visitor.visitChildren(self)




    def general_set_function(self):

        localctx = SQLParser.General_set_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_general_set_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 897
            self.set_function_type()
            self.state = 898
            self.match(SQLParser.LEFT_PAREN)
            self.state = 900
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.ALL or _la==SQLParser.DISTINCT:
                self.state = 899
                self.set_qualifier()


            self.state = 902
            self.value_expression()
            self.state = 903
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_function_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Set_function_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def AVG(self):
            return self.getToken(SQLParser.AVG, 0)

        def MAX(self):
            return self.getToken(SQLParser.MAX, 0)

        def MIN(self):
            return self.getToken(SQLParser.MIN, 0)

        def SUM(self):
            return self.getToken(SQLParser.SUM, 0)

        def EVERY(self):
            return self.getToken(SQLParser.EVERY, 0)

        def ANY(self):
            return self.getToken(SQLParser.ANY, 0)

        def SOME(self):
            return self.getToken(SQLParser.SOME, 0)

        def COUNT(self):
            return self.getToken(SQLParser.COUNT, 0)

        def STDDEV_POP(self):
            return self.getToken(SQLParser.STDDEV_POP, 0)

        def STDDEV_SAMP(self):
            return self.getToken(SQLParser.STDDEV_SAMP, 0)

        def VAR_SAMP(self):
            return self.getToken(SQLParser.VAR_SAMP, 0)

        def VAR_POP(self):
            return self.getToken(SQLParser.VAR_POP, 0)

        def COLLECT(self):
            return self.getToken(SQLParser.COLLECT, 0)

        def FUSION(self):
            return self.getToken(SQLParser.FUSION, 0)

        def INTERSECTION(self):
            return self.getToken(SQLParser.INTERSECTION, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_set_function_type

        def accept(self, visitor):
            if hasattr(visitor, "visitSet_function_type"):
                return visitor.visitSet_function_type(self)
            else:
                return visitor.visitChildren(self)




    def set_function_type(self):

        localctx = SQLParser.Set_function_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_set_function_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 905
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SQLParser.ANY) | (1 << SQLParser.SOME) | (1 << SQLParser.AVG) | (1 << SQLParser.COLLECT) | (1 << SQLParser.COUNT))) != 0) or ((((_la - 71)) & ~0x3f) == 0 and ((1 << (_la - 71)) & ((1 << (SQLParser.EVERY - 71)) | (1 << (SQLParser.FUSION - 71)) | (1 << (SQLParser.INTERSECTION - 71)) | (1 << (SQLParser.MAX - 71)) | (1 << (SQLParser.MIN - 71)) | (1 << (SQLParser.STDDEV_POP - 71)) | (1 << (SQLParser.STDDEV_SAMP - 71)) | (1 << (SQLParser.SUM - 71)) | (1 << (SQLParser.VAR_SAMP - 71)) | (1 << (SQLParser.VAR_POP - 71)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Filter_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Filter_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FILTER(self):
            return self.getToken(SQLParser.FILTER, 0)

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def WHERE(self):
            return self.getToken(SQLParser.WHERE, 0)

        def search_condition(self):
            return self.getTypedRuleContext(SQLParser.Search_conditionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_filter_clause

        def accept(self, visitor):
            if hasattr(visitor, "visitFilter_clause"):
                return visitor.visitFilter_clause(self)
            else:
                return visitor.visitChildren(self)




    def filter_clause(self):

        localctx = SQLParser.Filter_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_filter_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 907
            self.match(SQLParser.FILTER)
            self.state = 908
            self.match(SQLParser.LEFT_PAREN)
            self.state = 909
            self.match(SQLParser.WHERE)
            self.state = 910
            self.search_condition()
            self.state = 911
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Grouping_operationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Grouping_operationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def GROUPING(self):
            return self.getToken(SQLParser.GROUPING, 0)

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def column_reference_list(self):
            return self.getTypedRuleContext(SQLParser.Column_reference_listContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_grouping_operation

        def accept(self, visitor):
            if hasattr(visitor, "visitGrouping_operation"):
                return visitor.visitGrouping_operation(self)
            else:
                return visitor.visitChildren(self)




    def grouping_operation(self):

        localctx = SQLParser.Grouping_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_grouping_operation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 913
            self.match(SQLParser.GROUPING)
            self.state = 914
            self.match(SQLParser.LEFT_PAREN)
            self.state = 915
            self.column_reference_list()
            self.state = 916
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Case_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Case_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def case_specification(self):
            return self.getTypedRuleContext(SQLParser.Case_specificationContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_case_expression

        def accept(self, visitor):
            if hasattr(visitor, "visitCase_expression"):
                return visitor.visitCase_expression(self)
            else:
                return visitor.visitChildren(self)




    def case_expression(self):

        localctx = SQLParser.Case_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_case_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 918
            self.case_specification()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Case_abbreviationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Case_abbreviationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NULLIF(self):
            return self.getToken(SQLParser.NULLIF, 0)

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def numeric_value_expression(self):
            return self.getTypedRuleContext(SQLParser.Numeric_value_expressionContext,0)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def boolean_value_expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Boolean_value_expressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.Boolean_value_expressionContext,i)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def COALESCE(self):
            return self.getToken(SQLParser.COALESCE, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_case_abbreviation

        def accept(self, visitor):
            if hasattr(visitor, "visitCase_abbreviation"):
                return visitor.visitCase_abbreviation(self)
            else:
                return visitor.visitChildren(self)




    def case_abbreviation(self):

        localctx = SQLParser.Case_abbreviationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_case_abbreviation)
        self._la = 0 # Token type
        try:
            self.state = 938
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.NULLIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 920
                self.match(SQLParser.NULLIF)
                self.state = 921
                self.match(SQLParser.LEFT_PAREN)
                self.state = 922
                self.numeric_value_expression()
                self.state = 923
                self.match(SQLParser.COMMA)
                self.state = 924
                self.boolean_value_expression()
                self.state = 925
                self.match(SQLParser.RIGHT_PAREN)
                pass
            elif token in [SQLParser.COALESCE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 927
                self.match(SQLParser.COALESCE)
                self.state = 928
                self.match(SQLParser.LEFT_PAREN)
                self.state = 929
                self.numeric_value_expression()
                self.state = 932 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 930
                    self.match(SQLParser.COMMA)
                    self.state = 931
                    self.boolean_value_expression()
                    self.state = 934 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==SQLParser.COMMA):
                        break

                self.state = 936
                self.match(SQLParser.RIGHT_PAREN)
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

    class Case_specificationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Case_specificationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def simple_case(self):
            return self.getTypedRuleContext(SQLParser.Simple_caseContext,0)


        def searched_case(self):
            return self.getTypedRuleContext(SQLParser.Searched_caseContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_case_specification

        def accept(self, visitor):
            if hasattr(visitor, "visitCase_specification"):
                return visitor.visitCase_specification(self)
            else:
                return visitor.visitChildren(self)




    def case_specification(self):

        localctx = SQLParser.Case_specificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_case_specification)
        try:
            self.state = 942
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 940
                self.simple_case()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 941
                self.searched_case()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Simple_caseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Simple_caseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(SQLParser.CASE, 0)

        def boolean_value_expression(self):
            return self.getTypedRuleContext(SQLParser.Boolean_value_expressionContext,0)


        def END(self):
            return self.getToken(SQLParser.END, 0)

        def simple_when_clause(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Simple_when_clauseContext)
            else:
                return self.getTypedRuleContext(SQLParser.Simple_when_clauseContext,i)


        def else_clause(self):
            return self.getTypedRuleContext(SQLParser.Else_clauseContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_simple_case

        def accept(self, visitor):
            if hasattr(visitor, "visitSimple_case"):
                return visitor.visitSimple_case(self)
            else:
                return visitor.visitChildren(self)




    def simple_case(self):

        localctx = SQLParser.Simple_caseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_simple_case)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 944
            self.match(SQLParser.CASE)
            self.state = 945
            self.boolean_value_expression()
            self.state = 947 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 946
                self.simple_when_clause()
                self.state = 949 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SQLParser.WHEN):
                    break

            self.state = 952
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.ELSE:
                self.state = 951
                self.else_clause()


            self.state = 954
            self.match(SQLParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Searched_caseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Searched_caseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(SQLParser.CASE, 0)

        def END(self):
            return self.getToken(SQLParser.END, 0)

        def searched_when_clause(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Searched_when_clauseContext)
            else:
                return self.getTypedRuleContext(SQLParser.Searched_when_clauseContext,i)


        def else_clause(self):
            return self.getTypedRuleContext(SQLParser.Else_clauseContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_searched_case

        def accept(self, visitor):
            if hasattr(visitor, "visitSearched_case"):
                return visitor.visitSearched_case(self)
            else:
                return visitor.visitChildren(self)




    def searched_case(self):

        localctx = SQLParser.Searched_caseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_searched_case)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 956
            self.match(SQLParser.CASE)
            self.state = 958 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 957
                self.searched_when_clause()
                self.state = 960 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SQLParser.WHEN):
                    break

            self.state = 963
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.ELSE:
                self.state = 962
                self.else_clause()


            self.state = 965
            self.match(SQLParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Simple_when_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Simple_when_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WHEN(self):
            return self.getToken(SQLParser.WHEN, 0)

        def search_condition(self):
            return self.getTypedRuleContext(SQLParser.Search_conditionContext,0)


        def THEN(self):
            return self.getToken(SQLParser.THEN, 0)

        def result(self):
            return self.getTypedRuleContext(SQLParser.ResultContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_simple_when_clause

        def accept(self, visitor):
            if hasattr(visitor, "visitSimple_when_clause"):
                return visitor.visitSimple_when_clause(self)
            else:
                return visitor.visitChildren(self)




    def simple_when_clause(self):

        localctx = SQLParser.Simple_when_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_simple_when_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 967
            self.match(SQLParser.WHEN)
            self.state = 968
            self.search_condition()
            self.state = 969
            self.match(SQLParser.THEN)
            self.state = 970
            self.result()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Searched_when_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Searched_when_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.c = None # Search_conditionContext
            self.r = None # ResultContext

        def WHEN(self):
            return self.getToken(SQLParser.WHEN, 0)

        def THEN(self):
            return self.getToken(SQLParser.THEN, 0)

        def search_condition(self):
            return self.getTypedRuleContext(SQLParser.Search_conditionContext,0)


        def result(self):
            return self.getTypedRuleContext(SQLParser.ResultContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_searched_when_clause

        def accept(self, visitor):
            if hasattr(visitor, "visitSearched_when_clause"):
                return visitor.visitSearched_when_clause(self)
            else:
                return visitor.visitChildren(self)




    def searched_when_clause(self):

        localctx = SQLParser.Searched_when_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_searched_when_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 972
            self.match(SQLParser.WHEN)
            self.state = 973
            localctx.c = self.search_condition()
            self.state = 974
            self.match(SQLParser.THEN)
            self.state = 975
            localctx.r = self.result()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Else_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Else_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.r = None # ResultContext

        def ELSE(self):
            return self.getToken(SQLParser.ELSE, 0)

        def result(self):
            return self.getTypedRuleContext(SQLParser.ResultContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_else_clause

        def accept(self, visitor):
            if hasattr(visitor, "visitElse_clause"):
                return visitor.visitElse_clause(self)
            else:
                return visitor.visitChildren(self)




    def else_clause(self):

        localctx = SQLParser.Else_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_else_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 977
            self.match(SQLParser.ELSE)
            self.state = 978
            localctx.r = self.result()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ResultContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.ResultContext, self).__init__(parent, invokingState)
            self.parser = parser

        def value_expression(self):
            return self.getTypedRuleContext(SQLParser.Value_expressionContext,0)


        def NULL(self):
            return self.getToken(SQLParser.NULL, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_result

        def accept(self, visitor):
            if hasattr(visitor, "visitResult"):
                return visitor.visitResult(self)
            else:
                return visitor.visitChildren(self)




    def result(self):

        localctx = SQLParser.ResultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_result)
        try:
            self.state = 982
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 980
                self.value_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 981
                self.match(SQLParser.NULL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Cast_specificationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Cast_specificationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CAST(self):
            return self.getToken(SQLParser.CAST, 0)

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def cast_operand(self):
            return self.getTypedRuleContext(SQLParser.Cast_operandContext,0)


        def AS(self):
            return self.getToken(SQLParser.AS, 0)

        def cast_target(self):
            return self.getTypedRuleContext(SQLParser.Cast_targetContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_cast_specification

        def accept(self, visitor):
            if hasattr(visitor, "visitCast_specification"):
                return visitor.visitCast_specification(self)
            else:
                return visitor.visitChildren(self)




    def cast_specification(self):

        localctx = SQLParser.Cast_specificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_cast_specification)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 984
            self.match(SQLParser.CAST)
            self.state = 985
            self.match(SQLParser.LEFT_PAREN)
            self.state = 986
            self.cast_operand()
            self.state = 987
            self.match(SQLParser.AS)
            self.state = 988
            self.cast_target()
            self.state = 989
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Cast_operandContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Cast_operandContext, self).__init__(parent, invokingState)
            self.parser = parser

        def value_expression(self):
            return self.getTypedRuleContext(SQLParser.Value_expressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_cast_operand

        def accept(self, visitor):
            if hasattr(visitor, "visitCast_operand"):
                return visitor.visitCast_operand(self)
            else:
                return visitor.visitChildren(self)




    def cast_operand(self):

        localctx = SQLParser.Cast_operandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_cast_operand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 991
            self.value_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Cast_targetContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Cast_targetContext, self).__init__(parent, invokingState)
            self.parser = parser

        def data_type(self):
            return self.getTypedRuleContext(SQLParser.Data_typeContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_cast_target

        def accept(self, visitor):
            if hasattr(visitor, "visitCast_target"):
                return visitor.visitCast_target(self)
            else:
                return visitor.visitChildren(self)




    def cast_target(self):

        localctx = SQLParser.Cast_targetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_cast_target)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 993
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Value_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Value_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def common_value_expression(self):
            return self.getTypedRuleContext(SQLParser.Common_value_expressionContext,0)


        def row_value_expression(self):
            return self.getTypedRuleContext(SQLParser.Row_value_expressionContext,0)


        def boolean_value_expression(self):
            return self.getTypedRuleContext(SQLParser.Boolean_value_expressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_value_expression

        def accept(self, visitor):
            if hasattr(visitor, "visitValue_expression"):
                return visitor.visitValue_expression(self)
            else:
                return visitor.visitChildren(self)




    def value_expression(self):

        localctx = SQLParser.Value_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_value_expression)
        try:
            self.state = 998
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 995
                self.common_value_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 996
                self.row_value_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 997
                self.boolean_value_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Common_value_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Common_value_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def numeric_value_expression(self):
            return self.getTypedRuleContext(SQLParser.Numeric_value_expressionContext,0)


        def string_value_expression(self):
            return self.getTypedRuleContext(SQLParser.String_value_expressionContext,0)


        def NULL(self):
            return self.getToken(SQLParser.NULL, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_common_value_expression

        def accept(self, visitor):
            if hasattr(visitor, "visitCommon_value_expression"):
                return visitor.visitCommon_value_expression(self)
            else:
                return visitor.visitChildren(self)




    def common_value_expression(self):

        localctx = SQLParser.Common_value_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_common_value_expression)
        try:
            self.state = 1003
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1000
                self.numeric_value_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1001
                self.string_value_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1002
                self.match(SQLParser.NULL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Numeric_value_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Numeric_value_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.left = None # TermContext
            self.right = None # TermContext

        def term(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.TermContext)
            else:
                return self.getTypedRuleContext(SQLParser.TermContext,i)


        def PLUS(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.PLUS)
            else:
                return self.getToken(SQLParser.PLUS, i)

        def MINUS(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.MINUS)
            else:
                return self.getToken(SQLParser.MINUS, i)

        def getRuleIndex(self):
            return SQLParser.RULE_numeric_value_expression

        def accept(self, visitor):
            if hasattr(visitor, "visitNumeric_value_expression"):
                return visitor.visitNumeric_value_expression(self)
            else:
                return visitor.visitChildren(self)




    def numeric_value_expression(self):

        localctx = SQLParser.Numeric_value_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_numeric_value_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1005
            localctx.left = self.term()
            self.state = 1010
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.PLUS or _la==SQLParser.MINUS:
                self.state = 1006
                _la = self._input.LA(1)
                if not(_la==SQLParser.PLUS or _la==SQLParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 1007
                localctx.right = self.term()
                self.state = 1012
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.TermContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.left = None # FactorContext
            self.right = None # FactorContext

        def factor(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.FactorContext)
            else:
                return self.getTypedRuleContext(SQLParser.FactorContext,i)


        def MULTIPLY(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.MULTIPLY)
            else:
                return self.getToken(SQLParser.MULTIPLY, i)

        def DIVIDE(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.DIVIDE)
            else:
                return self.getToken(SQLParser.DIVIDE, i)

        def MODULAR(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.MODULAR)
            else:
                return self.getToken(SQLParser.MODULAR, i)

        def getRuleIndex(self):
            return SQLParser.RULE_term

        def accept(self, visitor):
            if hasattr(visitor, "visitTerm"):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = SQLParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1013
            localctx.left = self.factor()
            self.state = 1018
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 188)) & ~0x3f) == 0 and ((1 << (_la - 188)) & ((1 << (SQLParser.MULTIPLY - 188)) | (1 << (SQLParser.DIVIDE - 188)) | (1 << (SQLParser.MODULAR - 188)))) != 0):
                self.state = 1014
                _la = self._input.LA(1)
                if not(((((_la - 188)) & ~0x3f) == 0 and ((1 << (_la - 188)) & ((1 << (SQLParser.MULTIPLY - 188)) | (1 << (SQLParser.DIVIDE - 188)) | (1 << (SQLParser.MODULAR - 188)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 1015
                localctx.right = self.factor()
                self.state = 1020
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.FactorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def numeric_primary(self):
            return self.getTypedRuleContext(SQLParser.Numeric_primaryContext,0)


        def sign(self):
            return self.getTypedRuleContext(SQLParser.SignContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_factor

        def accept(self, visitor):
            if hasattr(visitor, "visitFactor"):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = SQLParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1022
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.PLUS or _la==SQLParser.MINUS:
                self.state = 1021
                self.sign()


            self.state = 1024
            self.numeric_primary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.ArrayContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def numeric_value_expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Numeric_value_expressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.Numeric_value_expressionContext,i)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_array

        def accept(self, visitor):
            if hasattr(visitor, "visitArray"):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = SQLParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1026
            self.match(SQLParser.LEFT_PAREN)
            self.state = 1027
            self.numeric_value_expression()
            self.state = 1032
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.COMMA:
                self.state = 1028
                self.match(SQLParser.COMMA)
                self.state = 1029
                self.numeric_value_expression()
                self.state = 1034
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1035
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Numeric_primaryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Numeric_primaryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def value_expression_primary(self):
            return self.getTypedRuleContext(SQLParser.Value_expression_primaryContext,0)


        def CAST_EXPRESSION(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.CAST_EXPRESSION)
            else:
                return self.getToken(SQLParser.CAST_EXPRESSION, i)

        def cast_target(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Cast_targetContext)
            else:
                return self.getTypedRuleContext(SQLParser.Cast_targetContext,i)


        def numeric_value_function(self):
            return self.getTypedRuleContext(SQLParser.Numeric_value_functionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_numeric_primary

        def accept(self, visitor):
            if hasattr(visitor, "visitNumeric_primary"):
                return visitor.visitNumeric_primary(self)
            else:
                return visitor.visitChildren(self)




    def numeric_primary(self):

        localctx = SQLParser.Numeric_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_numeric_primary)
        self._la = 0 # Token type
        try:
            self.state = 1046
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,88,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1037
                self.value_expression_primary()
                self.state = 1042
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SQLParser.CAST_EXPRESSION:
                    self.state = 1038
                    self.match(SQLParser.CAST_EXPRESSION)
                    self.state = 1039
                    self.cast_target()
                    self.state = 1044
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1045
                self.numeric_value_function()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SignContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.SignContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(SQLParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(SQLParser.MINUS, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_sign

        def accept(self, visitor):
            if hasattr(visitor, "visitSign"):
                return visitor.visitSign(self)
            else:
                return visitor.visitChildren(self)




    def sign(self):

        localctx = SQLParser.SignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_sign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1048
            _la = self._input.LA(1)
            if not(_la==SQLParser.PLUS or _la==SQLParser.MINUS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Numeric_value_functionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Numeric_value_functionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def extract_expression(self):
            return self.getTypedRuleContext(SQLParser.Extract_expressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_numeric_value_function

        def accept(self, visitor):
            if hasattr(visitor, "visitNumeric_value_function"):
                return visitor.visitNumeric_value_function(self)
            else:
                return visitor.visitChildren(self)




    def numeric_value_function(self):

        localctx = SQLParser.Numeric_value_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_numeric_value_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1050
            self.extract_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Extract_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Extract_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.extract_field_string = None # Extract_fieldContext

        def EXTRACT(self):
            return self.getToken(SQLParser.EXTRACT, 0)

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def FROM(self):
            return self.getToken(SQLParser.FROM, 0)

        def extract_source(self):
            return self.getTypedRuleContext(SQLParser.Extract_sourceContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def extract_field(self):
            return self.getTypedRuleContext(SQLParser.Extract_fieldContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_extract_expression

        def accept(self, visitor):
            if hasattr(visitor, "visitExtract_expression"):
                return visitor.visitExtract_expression(self)
            else:
                return visitor.visitChildren(self)




    def extract_expression(self):

        localctx = SQLParser.Extract_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_extract_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1052
            self.match(SQLParser.EXTRACT)
            self.state = 1053
            self.match(SQLParser.LEFT_PAREN)
            self.state = 1054
            localctx.extract_field_string = self.extract_field()
            self.state = 1055
            self.match(SQLParser.FROM)
            self.state = 1056
            self.extract_source()
            self.state = 1057
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Extract_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Extract_fieldContext, self).__init__(parent, invokingState)
            self.parser = parser

        def primary_datetime_field(self):
            return self.getTypedRuleContext(SQLParser.Primary_datetime_fieldContext,0)


        def time_zone_field(self):
            return self.getTypedRuleContext(SQLParser.Time_zone_fieldContext,0)


        def extended_datetime_field(self):
            return self.getTypedRuleContext(SQLParser.Extended_datetime_fieldContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_extract_field

        def accept(self, visitor):
            if hasattr(visitor, "visitExtract_field"):
                return visitor.visitExtract_field(self)
            else:
                return visitor.visitChildren(self)




    def extract_field(self):

        localctx = SQLParser.Extract_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_extract_field)
        try:
            self.state = 1062
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.DAY, SQLParser.HOUR, SQLParser.MINUTE, SQLParser.MONTH, SQLParser.SECOND, SQLParser.YEAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1059
                self.primary_datetime_field()
                pass
            elif token in [SQLParser.TIMEZONE, SQLParser.TIMEZONE_HOUR, SQLParser.TIMEZONE_MINUTE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1060
                self.time_zone_field()
                pass
            elif token in [SQLParser.CENTURY, SQLParser.DECADE, SQLParser.DOW, SQLParser.DOY, SQLParser.EPOCH, SQLParser.ISODOW, SQLParser.ISOYEAR, SQLParser.MICROSECONDS, SQLParser.MILLENNIUM, SQLParser.MILLISECONDS, SQLParser.QUARTER, SQLParser.WEEK]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1061
                self.extended_datetime_field()
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

    class Time_zone_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Time_zone_fieldContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TIMEZONE(self):
            return self.getToken(SQLParser.TIMEZONE, 0)

        def TIMEZONE_HOUR(self):
            return self.getToken(SQLParser.TIMEZONE_HOUR, 0)

        def TIMEZONE_MINUTE(self):
            return self.getToken(SQLParser.TIMEZONE_MINUTE, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_time_zone_field

        def accept(self, visitor):
            if hasattr(visitor, "visitTime_zone_field"):
                return visitor.visitTime_zone_field(self)
            else:
                return visitor.visitChildren(self)




    def time_zone_field(self):

        localctx = SQLParser.Time_zone_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_time_zone_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1064
            _la = self._input.LA(1)
            if not(((((_la - 120)) & ~0x3f) == 0 and ((1 << (_la - 120)) & ((1 << (SQLParser.TIMEZONE - 120)) | (1 << (SQLParser.TIMEZONE_HOUR - 120)) | (1 << (SQLParser.TIMEZONE_MINUTE - 120)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Extract_sourceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Extract_sourceContext, self).__init__(parent, invokingState)
            self.parser = parser

        def column_reference(self):
            return self.getTypedRuleContext(SQLParser.Column_referenceContext,0)


        def datetime_literal(self):
            return self.getTypedRuleContext(SQLParser.Datetime_literalContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_extract_source

        def accept(self, visitor):
            if hasattr(visitor, "visitExtract_source"):
                return visitor.visitExtract_source(self)
            else:
                return visitor.visitChildren(self)




    def extract_source(self):

        localctx = SQLParser.Extract_sourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_extract_source)
        try:
            self.state = 1068
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,90,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1066
                self.column_reference()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1067
                self.datetime_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class String_value_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.String_value_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def character_value_expression(self):
            return self.getTypedRuleContext(SQLParser.Character_value_expressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_string_value_expression

        def accept(self, visitor):
            if hasattr(visitor, "visitString_value_expression"):
                return visitor.visitString_value_expression(self)
            else:
                return visitor.visitChildren(self)




    def string_value_expression(self):

        localctx = SQLParser.String_value_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_string_value_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1070
            self.character_value_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Character_value_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Character_value_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def character_factor(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Character_factorContext)
            else:
                return self.getTypedRuleContext(SQLParser.Character_factorContext,i)


        def CONCATENATION_OPERATOR(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.CONCATENATION_OPERATOR)
            else:
                return self.getToken(SQLParser.CONCATENATION_OPERATOR, i)

        def getRuleIndex(self):
            return SQLParser.RULE_character_value_expression

        def accept(self, visitor):
            if hasattr(visitor, "visitCharacter_value_expression"):
                return visitor.visitCharacter_value_expression(self)
            else:
                return visitor.visitChildren(self)




    def character_value_expression(self):

        localctx = SQLParser.Character_value_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_character_value_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1072
            self.character_factor()
            self.state = 1077
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.CONCATENATION_OPERATOR:
                self.state = 1073
                self.match(SQLParser.CONCATENATION_OPERATOR)
                self.state = 1074
                self.character_factor()
                self.state = 1079
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Character_factorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Character_factorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def character_primary(self):
            return self.getTypedRuleContext(SQLParser.Character_primaryContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_character_factor

        def accept(self, visitor):
            if hasattr(visitor, "visitCharacter_factor"):
                return visitor.visitCharacter_factor(self)
            else:
                return visitor.visitChildren(self)




    def character_factor(self):

        localctx = SQLParser.Character_factorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_character_factor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1080
            self.character_primary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Character_primaryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Character_primaryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def value_expression_primary(self):
            return self.getTypedRuleContext(SQLParser.Value_expression_primaryContext,0)


        def string_value_function(self):
            return self.getTypedRuleContext(SQLParser.String_value_functionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_character_primary

        def accept(self, visitor):
            if hasattr(visitor, "visitCharacter_primary"):
                return visitor.visitCharacter_primary(self)
            else:
                return visitor.visitChildren(self)




    def character_primary(self):

        localctx = SQLParser.Character_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_character_primary)
        try:
            self.state = 1084
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,92,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1082
                self.value_expression_primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1083
                self.string_value_function()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class String_value_functionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.String_value_functionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def trim_function(self):
            return self.getTypedRuleContext(SQLParser.Trim_functionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_string_value_function

        def accept(self, visitor):
            if hasattr(visitor, "visitString_value_function"):
                return visitor.visitString_value_function(self)
            else:
                return visitor.visitChildren(self)




    def string_value_function(self):

        localctx = SQLParser.String_value_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_string_value_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1086
            self.trim_function()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Trim_functionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Trim_functionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TRIM(self):
            return self.getToken(SQLParser.TRIM, 0)

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def trim_operands(self):
            return self.getTypedRuleContext(SQLParser.Trim_operandsContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_trim_function

        def accept(self, visitor):
            if hasattr(visitor, "visitTrim_function"):
                return visitor.visitTrim_function(self)
            else:
                return visitor.visitChildren(self)




    def trim_function(self):

        localctx = SQLParser.Trim_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_trim_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1088
            self.match(SQLParser.TRIM)
            self.state = 1089
            self.match(SQLParser.LEFT_PAREN)
            self.state = 1090
            self.trim_operands()
            self.state = 1091
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Trim_operandsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Trim_operandsContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.trim_character = None # Character_value_expressionContext
            self.trim_source = None # Character_value_expressionContext

        def character_value_expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Character_value_expressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.Character_value_expressionContext,i)


        def FROM(self):
            return self.getToken(SQLParser.FROM, 0)

        def trim_specification(self):
            return self.getTypedRuleContext(SQLParser.Trim_specificationContext,0)


        def COMMA(self):
            return self.getToken(SQLParser.COMMA, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_trim_operands

        def accept(self, visitor):
            if hasattr(visitor, "visitTrim_operands"):
                return visitor.visitTrim_operands(self)
            else:
                return visitor.visitChildren(self)




    def trim_operands(self):

        localctx = SQLParser.Trim_operandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_trim_operands)
        self._la = 0 # Token type
        try:
            self.state = 1107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,96,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1100
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,95,self._ctx)
                if la_ == 1:
                    self.state = 1094
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SQLParser.BOTH) | (1 << SQLParser.LEADING) | (1 << SQLParser.TRAILING))) != 0):
                        self.state = 1093
                        self.trim_specification()


                    self.state = 1097
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SQLParser.ANY) | (1 << SQLParser.CASE) | (1 << SQLParser.CAST) | (1 << SQLParser.FALSE) | (1 << SQLParser.LEFT) | (1 << SQLParser.RIGHT) | (1 << SQLParser.SOME) | (1 << SQLParser.TRUE) | (1 << SQLParser.AVG) | (1 << SQLParser.BETWEEN) | (1 << SQLParser.BY) | (1 << SQLParser.CENTURY) | (1 << SQLParser.CHARACTER) | (1 << SQLParser.COLLECT) | (1 << SQLParser.COALESCE) | (1 << SQLParser.COLUMN) | (1 << SQLParser.COUNT) | (1 << SQLParser.CUBE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (SQLParser.DAY - 64)) | (1 << (SQLParser.DEC - 64)) | (1 << (SQLParser.DECADE - 64)) | (1 << (SQLParser.DOW - 64)) | (1 << (SQLParser.DOY - 64)) | (1 << (SQLParser.DROP - 64)) | (1 << (SQLParser.EPOCH - 64)) | (1 << (SQLParser.EVERY - 64)) | (1 << (SQLParser.EXISTS - 64)) | (1 << (SQLParser.EXTERNAL - 64)) | (1 << (SQLParser.EXTRACT - 64)) | (1 << (SQLParser.FILTER - 64)) | (1 << (SQLParser.FIRST - 64)) | (1 << (SQLParser.FORMAT - 64)) | (1 << (SQLParser.FUSION - 64)) | (1 << (SQLParser.GROUPING - 64)) | (1 << (SQLParser.HASH - 64)) | (1 << (SQLParser.INDEX - 64)) | (1 << (SQLParser.INSERT - 64)) | (1 << (SQLParser.INTERSECTION - 64)) | (1 << (SQLParser.ISODOW - 64)) | (1 << (SQLParser.ISOYEAR - 64)) | (1 << (SQLParser.LAST - 64)) | (1 << (SQLParser.LESS - 64)) | (1 << (SQLParser.LIST - 64)) | (1 << (SQLParser.LOCATION - 64)) | (1 << (SQLParser.MAX - 64)) | (1 << (SQLParser.MAXVALUE - 64)) | (1 << (SQLParser.MICROSECONDS - 64)) | (1 << (SQLParser.MILLENNIUM - 64)) | (1 << (SQLParser.MILLISECONDS - 64)) | (1 << (SQLParser.MIN - 64)) | (1 << (SQLParser.MINUTE - 64)) | (1 << (SQLParser.MONTH - 64)) | (1 << (SQLParser.NATIONAL - 64)) | (1 << (SQLParser.NULLIF - 64)) | (1 << (SQLParser.OVERWRITE - 64)) | (1 << (SQLParser.PARTITION - 64)) | (1 << (SQLParser.PARTITIONS - 64)) | (1 << (SQLParser.PRECISION - 64)) | (1 << (SQLParser.PURGE - 64)) | (1 << (SQLParser.QUARTER - 64)) | (1 << (SQLParser.RANGE - 64)) | (1 << (SQLParser.REGEXP - 64)) | (1 << (SQLParser.RLIKE - 64)) | (1 << (SQLParser.ROLLUP - 64)) | (1 << (SQLParser.SECOND - 64)) | (1 << (SQLParser.SET - 64)) | (1 << (SQLParser.SIMILAR - 64)) | (1 << (SQLParser.STDDEV_POP - 64)) | (1 << (SQLParser.STDDEV_SAMP - 64)) | (1 << (SQLParser.SUBPARTITION - 64)) | (1 << (SQLParser.SUM - 64)) | (1 << (SQLParser.TABLESPACE - 64)) | (1 << (SQLParser.THAN - 64)) | (1 << (SQLParser.TIMEZONE - 64)) | (1 << (SQLParser.TIMEZONE_HOUR - 64)) | (1 << (SQLParser.TIMEZONE_MINUTE - 64)) | (1 << (SQLParser.TRIM - 64)) | (1 << (SQLParser.TO - 64)) | (1 << (SQLParser.UNKNOWN - 64)) | (1 << (SQLParser.VALUES - 64)) | (1 << (SQLParser.VAR_SAMP - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (SQLParser.VAR_POP - 128)) | (1 << (SQLParser.VARYING - 128)) | (1 << (SQLParser.WEEK - 128)) | (1 << (SQLParser.YEAR - 128)) | (1 << (SQLParser.ZONE - 128)) | (1 << (SQLParser.BOOLEAN - 128)) | (1 << (SQLParser.BOOL - 128)) | (1 << (SQLParser.BIT - 128)) | (1 << (SQLParser.VARBIT - 128)) | (1 << (SQLParser.INT1 - 128)) | (1 << (SQLParser.INT2 - 128)) | (1 << (SQLParser.INT4 - 128)) | (1 << (SQLParser.INT8 - 128)) | (1 << (SQLParser.TINYINT - 128)) | (1 << (SQLParser.SMALLINT - 128)) | (1 << (SQLParser.INT - 128)) | (1 << (SQLParser.INTEGER - 128)) | (1 << (SQLParser.BIGINT - 128)) | (1 << (SQLParser.FLOAT4 - 128)) | (1 << (SQLParser.FLOAT8 - 128)) | (1 << (SQLParser.REAL - 128)) | (1 << (SQLParser.FLOAT - 128)) | (1 << (SQLParser.DOUBLE - 128)) | (1 << (SQLParser.NUMERIC - 128)) | (1 << (SQLParser.DECIMAL - 128)) | (1 << (SQLParser.CHAR - 128)) | (1 << (SQLParser.VARCHAR - 128)) | (1 << (SQLParser.NCHAR - 128)) | (1 << (SQLParser.NVARCHAR - 128)) | (1 << (SQLParser.DATE - 128)) | (1 << (SQLParser.TIME - 128)) | (1 << (SQLParser.TIMETZ - 128)) | (1 << (SQLParser.TIMESTAMP - 128)) | (1 << (SQLParser.TIMESTAMPTZ - 128)) | (1 << (SQLParser.TEXT - 128)) | (1 << (SQLParser.VARBINARY - 128)) | (1 << (SQLParser.BLOB - 128)) | (1 << (SQLParser.BYTEA - 128)) | (1 << (SQLParser.INET4 - 128)) | (1 << (SQLParser.LEFT_PAREN - 128)))) != 0) or ((((_la - 196)) & ~0x3f) == 0 and ((1 << (_la - 196)) & ((1 << (SQLParser.NUMBER - 196)) | (1 << (SQLParser.REAL_NUMBER - 196)) | (1 << (SQLParser.Identifier - 196)) | (1 << (SQLParser.Character_String_Literal - 196)))) != 0):
                        self.state = 1096
                        localctx.trim_character = self.character_value_expression()


                    self.state = 1099
                    self.match(SQLParser.FROM)


                self.state = 1102
                localctx.trim_source = self.character_value_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1103
                localctx.trim_source = self.character_value_expression()
                self.state = 1104
                self.match(SQLParser.COMMA)
                self.state = 1105
                localctx.trim_character = self.character_value_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Trim_specificationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Trim_specificationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LEADING(self):
            return self.getToken(SQLParser.LEADING, 0)

        def TRAILING(self):
            return self.getToken(SQLParser.TRAILING, 0)

        def BOTH(self):
            return self.getToken(SQLParser.BOTH, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_trim_specification

        def accept(self, visitor):
            if hasattr(visitor, "visitTrim_specification"):
                return visitor.visitTrim_specification(self)
            else:
                return visitor.visitChildren(self)




    def trim_specification(self):

        localctx = SQLParser.Trim_specificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_trim_specification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1109
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SQLParser.BOTH) | (1 << SQLParser.LEADING) | (1 << SQLParser.TRAILING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Boolean_value_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Boolean_value_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def or_predicate(self):
            return self.getTypedRuleContext(SQLParser.Or_predicateContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_boolean_value_expression

        def accept(self, visitor):
            if hasattr(visitor, "visitBoolean_value_expression"):
                return visitor.visitBoolean_value_expression(self)
            else:
                return visitor.visitChildren(self)




    def boolean_value_expression(self):

        localctx = SQLParser.Boolean_value_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_boolean_value_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1111
            self.or_predicate()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Or_predicateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Or_predicateContext, self).__init__(parent, invokingState)
            self.parser = parser

        def and_predicate(self):
            return self.getTypedRuleContext(SQLParser.And_predicateContext,0)


        def OR(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.OR)
            else:
                return self.getToken(SQLParser.OR, i)

        def or_predicate(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Or_predicateContext)
            else:
                return self.getTypedRuleContext(SQLParser.Or_predicateContext,i)


        def getRuleIndex(self):
            return SQLParser.RULE_or_predicate

        def accept(self, visitor):
            if hasattr(visitor, "visitOr_predicate"):
                return visitor.visitOr_predicate(self)
            else:
                return visitor.visitChildren(self)




    def or_predicate(self):

        localctx = SQLParser.Or_predicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_or_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1113
            self.and_predicate()
            self.state = 1118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,97,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1114
                    self.match(SQLParser.OR)
                    self.state = 1115
                    self.or_predicate() 
                self.state = 1120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,97,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class And_predicateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.And_predicateContext, self).__init__(parent, invokingState)
            self.parser = parser

        def boolean_factor(self):
            return self.getTypedRuleContext(SQLParser.Boolean_factorContext,0)


        def AND(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.AND)
            else:
                return self.getToken(SQLParser.AND, i)

        def and_predicate(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.And_predicateContext)
            else:
                return self.getTypedRuleContext(SQLParser.And_predicateContext,i)


        def getRuleIndex(self):
            return SQLParser.RULE_and_predicate

        def accept(self, visitor):
            if hasattr(visitor, "visitAnd_predicate"):
                return visitor.visitAnd_predicate(self)
            else:
                return visitor.visitChildren(self)




    def and_predicate(self):

        localctx = SQLParser.And_predicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_and_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1121
            self.boolean_factor()
            self.state = 1126
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,98,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1122
                    self.match(SQLParser.AND)
                    self.state = 1123
                    self.and_predicate() 
                self.state = 1128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,98,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Boolean_factorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Boolean_factorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def boolean_test(self):
            return self.getTypedRuleContext(SQLParser.Boolean_testContext,0)


        def NOT(self):
            return self.getToken(SQLParser.NOT, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_boolean_factor

        def accept(self, visitor):
            if hasattr(visitor, "visitBoolean_factor"):
                return visitor.visitBoolean_factor(self)
            else:
                return visitor.visitChildren(self)




    def boolean_factor(self):

        localctx = SQLParser.Boolean_factorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_boolean_factor)
        try:
            self.state = 1132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,99,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1129
                self.boolean_test()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1130
                self.match(SQLParser.NOT)
                self.state = 1131
                self.boolean_test()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Boolean_testContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Boolean_testContext, self).__init__(parent, invokingState)
            self.parser = parser

        def boolean_primary(self):
            return self.getTypedRuleContext(SQLParser.Boolean_primaryContext,0)


        def is_clause(self):
            return self.getTypedRuleContext(SQLParser.Is_clauseContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_boolean_test

        def accept(self, visitor):
            if hasattr(visitor, "visitBoolean_test"):
                return visitor.visitBoolean_test(self)
            else:
                return visitor.visitChildren(self)




    def boolean_test(self):

        localctx = SQLParser.Boolean_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_boolean_test)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1134
            self.boolean_primary()
            self.state = 1136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.IS:
                self.state = 1135
                self.is_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Is_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Is_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t = None # Truth_valueContext

        def IS(self):
            return self.getToken(SQLParser.IS, 0)

        def truth_value(self):
            return self.getTypedRuleContext(SQLParser.Truth_valueContext,0)


        def NOT(self):
            return self.getToken(SQLParser.NOT, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_is_clause

        def accept(self, visitor):
            if hasattr(visitor, "visitIs_clause"):
                return visitor.visitIs_clause(self)
            else:
                return visitor.visitChildren(self)




    def is_clause(self):

        localctx = SQLParser.Is_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_is_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1138
            self.match(SQLParser.IS)
            self.state = 1140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.NOT:
                self.state = 1139
                self.match(SQLParser.NOT)


            self.state = 1142
            localctx.t = self.truth_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Truth_valueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Truth_valueContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(SQLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(SQLParser.FALSE, 0)

        def UNKNOWN(self):
            return self.getToken(SQLParser.UNKNOWN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_truth_value

        def accept(self, visitor):
            if hasattr(visitor, "visitTruth_value"):
                return visitor.visitTruth_value(self)
            else:
                return visitor.visitChildren(self)




    def truth_value(self):

        localctx = SQLParser.Truth_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_truth_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1144
            _la = self._input.LA(1)
            if not(_la==SQLParser.FALSE or _la==SQLParser.TRUE or _la==SQLParser.UNKNOWN):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Boolean_primaryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Boolean_primaryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def predicate(self):
            return self.getTypedRuleContext(SQLParser.PredicateContext,0)


        def boolean_predicand(self):
            return self.getTypedRuleContext(SQLParser.Boolean_predicandContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_boolean_primary

        def accept(self, visitor):
            if hasattr(visitor, "visitBoolean_primary"):
                return visitor.visitBoolean_primary(self)
            else:
                return visitor.visitChildren(self)




    def boolean_primary(self):

        localctx = SQLParser.Boolean_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_boolean_primary)
        try:
            self.state = 1148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,102,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1146
                self.predicate()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1147
                self.boolean_predicand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Boolean_predicandContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Boolean_predicandContext, self).__init__(parent, invokingState)
            self.parser = parser

        def parenthesized_boolean_value_expression(self):
            return self.getTypedRuleContext(SQLParser.Parenthesized_boolean_value_expressionContext,0)


        def nonparenthesized_value_expression_primary(self):
            return self.getTypedRuleContext(SQLParser.Nonparenthesized_value_expression_primaryContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_boolean_predicand

        def accept(self, visitor):
            if hasattr(visitor, "visitBoolean_predicand"):
                return visitor.visitBoolean_predicand(self)
            else:
                return visitor.visitChildren(self)




    def boolean_predicand(self):

        localctx = SQLParser.Boolean_predicandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_boolean_predicand)
        try:
            self.state = 1152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,103,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1150
                self.parenthesized_boolean_value_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1151
                self.nonparenthesized_value_expression_primary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Parenthesized_boolean_value_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Parenthesized_boolean_value_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def boolean_value_expression(self):
            return self.getTypedRuleContext(SQLParser.Boolean_value_expressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_parenthesized_boolean_value_expression

        def accept(self, visitor):
            if hasattr(visitor, "visitParenthesized_boolean_value_expression"):
                return visitor.visitParenthesized_boolean_value_expression(self)
            else:
                return visitor.visitChildren(self)




    def parenthesized_boolean_value_expression(self):

        localctx = SQLParser.Parenthesized_boolean_value_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_parenthesized_boolean_value_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1154
            self.match(SQLParser.LEFT_PAREN)
            self.state = 1155
            self.boolean_value_expression()
            self.state = 1156
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Row_value_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Row_value_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def row_value_special_case(self):
            return self.getTypedRuleContext(SQLParser.Row_value_special_caseContext,0)


        def explicit_row_value_constructor(self):
            return self.getTypedRuleContext(SQLParser.Explicit_row_value_constructorContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_row_value_expression

        def accept(self, visitor):
            if hasattr(visitor, "visitRow_value_expression"):
                return visitor.visitRow_value_expression(self)
            else:
                return visitor.visitChildren(self)




    def row_value_expression(self):

        localctx = SQLParser.Row_value_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_row_value_expression)
        try:
            self.state = 1160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.ANY, SQLParser.CASE, SQLParser.CAST, SQLParser.FALSE, SQLParser.LEFT, SQLParser.RIGHT, SQLParser.SOME, SQLParser.TRUE, SQLParser.AVG, SQLParser.BETWEEN, SQLParser.BY, SQLParser.CENTURY, SQLParser.CHARACTER, SQLParser.COLLECT, SQLParser.COALESCE, SQLParser.COLUMN, SQLParser.COUNT, SQLParser.CUBE, SQLParser.DAY, SQLParser.DEC, SQLParser.DECADE, SQLParser.DOW, SQLParser.DOY, SQLParser.DROP, SQLParser.EPOCH, SQLParser.EVERY, SQLParser.EXISTS, SQLParser.EXTERNAL, SQLParser.EXTRACT, SQLParser.FILTER, SQLParser.FIRST, SQLParser.FORMAT, SQLParser.FUSION, SQLParser.GROUPING, SQLParser.HASH, SQLParser.INDEX, SQLParser.INSERT, SQLParser.INTERSECTION, SQLParser.ISODOW, SQLParser.ISOYEAR, SQLParser.LAST, SQLParser.LESS, SQLParser.LIST, SQLParser.LOCATION, SQLParser.MAX, SQLParser.MAXVALUE, SQLParser.MICROSECONDS, SQLParser.MILLENNIUM, SQLParser.MILLISECONDS, SQLParser.MIN, SQLParser.MINUTE, SQLParser.MONTH, SQLParser.NATIONAL, SQLParser.NULLIF, SQLParser.OVERWRITE, SQLParser.PARTITION, SQLParser.PARTITIONS, SQLParser.PRECISION, SQLParser.PURGE, SQLParser.QUARTER, SQLParser.RANGE, SQLParser.REGEXP, SQLParser.RLIKE, SQLParser.ROLLUP, SQLParser.SECOND, SQLParser.SET, SQLParser.SIMILAR, SQLParser.STDDEV_POP, SQLParser.STDDEV_SAMP, SQLParser.SUBPARTITION, SQLParser.SUM, SQLParser.TABLESPACE, SQLParser.THAN, SQLParser.TIMEZONE, SQLParser.TIMEZONE_HOUR, SQLParser.TIMEZONE_MINUTE, SQLParser.TRIM, SQLParser.TO, SQLParser.UNKNOWN, SQLParser.VALUES, SQLParser.VAR_SAMP, SQLParser.VAR_POP, SQLParser.VARYING, SQLParser.WEEK, SQLParser.YEAR, SQLParser.ZONE, SQLParser.BOOLEAN, SQLParser.BOOL, SQLParser.BIT, SQLParser.VARBIT, SQLParser.INT1, SQLParser.INT2, SQLParser.INT4, SQLParser.INT8, SQLParser.TINYINT, SQLParser.SMALLINT, SQLParser.INT, SQLParser.INTEGER, SQLParser.BIGINT, SQLParser.FLOAT4, SQLParser.FLOAT8, SQLParser.REAL, SQLParser.FLOAT, SQLParser.DOUBLE, SQLParser.NUMERIC, SQLParser.DECIMAL, SQLParser.CHAR, SQLParser.VARCHAR, SQLParser.NCHAR, SQLParser.NVARCHAR, SQLParser.DATE, SQLParser.TIME, SQLParser.TIMETZ, SQLParser.TIMESTAMP, SQLParser.TIMESTAMPTZ, SQLParser.TEXT, SQLParser.VARBINARY, SQLParser.BLOB, SQLParser.BYTEA, SQLParser.INET4, SQLParser.LEFT_PAREN, SQLParser.NUMBER, SQLParser.REAL_NUMBER, SQLParser.Identifier, SQLParser.Character_String_Literal]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1158
                self.row_value_special_case()
                pass
            elif token in [SQLParser.NULL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1159
                self.explicit_row_value_constructor()
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

    class Row_value_special_caseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Row_value_special_caseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def nonparenthesized_value_expression_primary(self):
            return self.getTypedRuleContext(SQLParser.Nonparenthesized_value_expression_primaryContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_row_value_special_case

        def accept(self, visitor):
            if hasattr(visitor, "visitRow_value_special_case"):
                return visitor.visitRow_value_special_case(self)
            else:
                return visitor.visitChildren(self)




    def row_value_special_case(self):

        localctx = SQLParser.Row_value_special_caseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_row_value_special_case)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1162
            self.nonparenthesized_value_expression_primary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Explicit_row_value_constructorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Explicit_row_value_constructorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NULL(self):
            return self.getToken(SQLParser.NULL, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_explicit_row_value_constructor

        def accept(self, visitor):
            if hasattr(visitor, "visitExplicit_row_value_constructor"):
                return visitor.visitExplicit_row_value_constructor(self)
            else:
                return visitor.visitChildren(self)




    def explicit_row_value_constructor(self):

        localctx = SQLParser.Explicit_row_value_constructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_explicit_row_value_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1164
            self.match(SQLParser.NULL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Row_value_predicandContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Row_value_predicandContext, self).__init__(parent, invokingState)
            self.parser = parser

        def row_value_special_case(self):
            return self.getTypedRuleContext(SQLParser.Row_value_special_caseContext,0)


        def row_value_constructor_predicand(self):
            return self.getTypedRuleContext(SQLParser.Row_value_constructor_predicandContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_row_value_predicand

        def accept(self, visitor):
            if hasattr(visitor, "visitRow_value_predicand"):
                return visitor.visitRow_value_predicand(self)
            else:
                return visitor.visitChildren(self)




    def row_value_predicand(self):

        localctx = SQLParser.Row_value_predicandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_row_value_predicand)
        try:
            self.state = 1168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,105,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1166
                self.row_value_special_case()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1167
                self.row_value_constructor_predicand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Row_value_constructor_predicandContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Row_value_constructor_predicandContext, self).__init__(parent, invokingState)
            self.parser = parser

        def common_value_expression(self):
            return self.getTypedRuleContext(SQLParser.Common_value_expressionContext,0)


        def boolean_predicand(self):
            return self.getTypedRuleContext(SQLParser.Boolean_predicandContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_row_value_constructor_predicand

        def accept(self, visitor):
            if hasattr(visitor, "visitRow_value_constructor_predicand"):
                return visitor.visitRow_value_constructor_predicand(self)
            else:
                return visitor.visitChildren(self)




    def row_value_constructor_predicand(self):

        localctx = SQLParser.Row_value_constructor_predicandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_row_value_constructor_predicand)
        try:
            self.state = 1172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,106,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1170
                self.common_value_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1171
                self.boolean_predicand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Table_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Table_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def from_clause(self):
            return self.getTypedRuleContext(SQLParser.From_clauseContext,0)


        def where_clause(self):
            return self.getTypedRuleContext(SQLParser.Where_clauseContext,0)


        def groupby_clause(self):
            return self.getTypedRuleContext(SQLParser.Groupby_clauseContext,0)


        def having_clause(self):
            return self.getTypedRuleContext(SQLParser.Having_clauseContext,0)


        def orderby_clause(self):
            return self.getTypedRuleContext(SQLParser.Orderby_clauseContext,0)


        def limit_clause(self):
            return self.getTypedRuleContext(SQLParser.Limit_clauseContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_table_expression

        def accept(self, visitor):
            if hasattr(visitor, "visitTable_expression"):
                return visitor.visitTable_expression(self)
            else:
                return visitor.visitChildren(self)




    def table_expression(self):

        localctx = SQLParser.Table_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_table_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1174
            self.from_clause()
            self.state = 1176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.WHERE:
                self.state = 1175
                self.where_clause()


            self.state = 1179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.GROUP:
                self.state = 1178
                self.groupby_clause()


            self.state = 1182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.HAVING:
                self.state = 1181
                self.having_clause()


            self.state = 1185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.ORDER:
                self.state = 1184
                self.orderby_clause()


            self.state = 1188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.LIMIT:
                self.state = 1187
                self.limit_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class From_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.From_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(SQLParser.FROM, 0)

        def table_reference_list(self):
            return self.getTypedRuleContext(SQLParser.Table_reference_listContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_from_clause

        def accept(self, visitor):
            if hasattr(visitor, "visitFrom_clause"):
                return visitor.visitFrom_clause(self)
            else:
                return visitor.visitChildren(self)




    def from_clause(self):

        localctx = SQLParser.From_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_from_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1190
            self.match(SQLParser.FROM)
            self.state = 1191
            self.table_reference_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Table_reference_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Table_reference_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def table_reference(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Table_referenceContext)
            else:
                return self.getTypedRuleContext(SQLParser.Table_referenceContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_table_reference_list

        def accept(self, visitor):
            if hasattr(visitor, "visitTable_reference_list"):
                return visitor.visitTable_reference_list(self)
            else:
                return visitor.visitChildren(self)




    def table_reference_list(self):

        localctx = SQLParser.Table_reference_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_table_reference_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1193
            self.table_reference()
            self.state = 1198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.COMMA:
                self.state = 1194
                self.match(SQLParser.COMMA)
                self.state = 1195
                self.table_reference()
                self.state = 1200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Table_referenceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Table_referenceContext, self).__init__(parent, invokingState)
            self.parser = parser

        def joined_table(self):
            return self.getTypedRuleContext(SQLParser.Joined_tableContext,0)


        def table_primary(self):
            return self.getTypedRuleContext(SQLParser.Table_primaryContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_table_reference

        def accept(self, visitor):
            if hasattr(visitor, "visitTable_reference"):
                return visitor.visitTable_reference(self)
            else:
                return visitor.visitChildren(self)




    def table_reference(self):

        localctx = SQLParser.Table_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_table_reference)
        try:
            self.state = 1203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,113,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1201
                self.joined_table()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1202
                self.table_primary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Joined_tableContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Joined_tableContext, self).__init__(parent, invokingState)
            self.parser = parser

        def table_primary(self):
            return self.getTypedRuleContext(SQLParser.Table_primaryContext,0)


        def joined_table_primary(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Joined_table_primaryContext)
            else:
                return self.getTypedRuleContext(SQLParser.Joined_table_primaryContext,i)


        def getRuleIndex(self):
            return SQLParser.RULE_joined_table

        def accept(self, visitor):
            if hasattr(visitor, "visitJoined_table"):
                return visitor.visitJoined_table(self)
            else:
                return visitor.visitChildren(self)




    def joined_table(self):

        localctx = SQLParser.Joined_tableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_joined_table)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1205
            self.table_primary()
            self.state = 1207 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 1206
                    self.joined_table_primary()

                else:
                    raise NoViableAltException(self)
                self.state = 1209 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,114,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Joined_table_primaryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Joined_table_primaryContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.right = None # Table_primaryContext
            self.t = None # Join_typeContext
            self.s = None # Join_specificationContext

        def CROSS(self):
            return self.getToken(SQLParser.CROSS, 0)

        def JOIN(self):
            return self.getToken(SQLParser.JOIN, 0)

        def table_primary(self):
            return self.getTypedRuleContext(SQLParser.Table_primaryContext,0)


        def join_specification(self):
            return self.getTypedRuleContext(SQLParser.Join_specificationContext,0)


        def join_type(self):
            return self.getTypedRuleContext(SQLParser.Join_typeContext,0)


        def NATURAL(self):
            return self.getToken(SQLParser.NATURAL, 0)

        def UNION(self):
            return self.getToken(SQLParser.UNION, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_joined_table_primary

        def accept(self, visitor):
            if hasattr(visitor, "visitJoined_table_primary"):
                return visitor.visitJoined_table_primary(self)
            else:
                return visitor.visitChildren(self)




    def joined_table_primary(self):

        localctx = SQLParser.Joined_table_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_joined_table_primary)
        self._la = 0 # Token type
        try:
            self.state = 1230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.CROSS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1211
                self.match(SQLParser.CROSS)
                self.state = 1212
                self.match(SQLParser.JOIN)
                self.state = 1213
                localctx.right = self.table_primary()
                pass
            elif token in [SQLParser.FULL, SQLParser.INNER, SQLParser.JOIN, SQLParser.LEFT, SQLParser.RIGHT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1215
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SQLParser.FULL) | (1 << SQLParser.INNER) | (1 << SQLParser.LEFT) | (1 << SQLParser.RIGHT))) != 0):
                    self.state = 1214
                    localctx.t = self.join_type()


                self.state = 1217
                self.match(SQLParser.JOIN)
                self.state = 1218
                localctx.right = self.table_primary()
                self.state = 1219
                localctx.s = self.join_specification()
                pass
            elif token in [SQLParser.NATURAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1221
                self.match(SQLParser.NATURAL)
                self.state = 1223
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SQLParser.FULL) | (1 << SQLParser.INNER) | (1 << SQLParser.LEFT) | (1 << SQLParser.RIGHT))) != 0):
                    self.state = 1222
                    localctx.t = self.join_type()


                self.state = 1225
                self.match(SQLParser.JOIN)
                self.state = 1226
                localctx.right = self.table_primary()
                pass
            elif token in [SQLParser.UNION]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1227
                self.match(SQLParser.UNION)
                self.state = 1228
                self.match(SQLParser.JOIN)
                self.state = 1229
                localctx.right = self.table_primary()
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

    class Cross_joinContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Cross_joinContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.r = None # Table_primaryContext

        def CROSS(self):
            return self.getToken(SQLParser.CROSS, 0)

        def JOIN(self):
            return self.getToken(SQLParser.JOIN, 0)

        def table_primary(self):
            return self.getTypedRuleContext(SQLParser.Table_primaryContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_cross_join

        def accept(self, visitor):
            if hasattr(visitor, "visitCross_join"):
                return visitor.visitCross_join(self)
            else:
                return visitor.visitChildren(self)




    def cross_join(self):

        localctx = SQLParser.Cross_joinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_cross_join)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1232
            self.match(SQLParser.CROSS)
            self.state = 1233
            self.match(SQLParser.JOIN)
            self.state = 1234
            localctx.r = self.table_primary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Qualified_joinContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Qualified_joinContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t = None # Join_typeContext
            self.r = None # Table_primaryContext
            self.s = None # Join_specificationContext

        def JOIN(self):
            return self.getToken(SQLParser.JOIN, 0)

        def table_primary(self):
            return self.getTypedRuleContext(SQLParser.Table_primaryContext,0)


        def join_specification(self):
            return self.getTypedRuleContext(SQLParser.Join_specificationContext,0)


        def join_type(self):
            return self.getTypedRuleContext(SQLParser.Join_typeContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_qualified_join

        def accept(self, visitor):
            if hasattr(visitor, "visitQualified_join"):
                return visitor.visitQualified_join(self)
            else:
                return visitor.visitChildren(self)




    def qualified_join(self):

        localctx = SQLParser.Qualified_joinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_qualified_join)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SQLParser.FULL) | (1 << SQLParser.INNER) | (1 << SQLParser.LEFT) | (1 << SQLParser.RIGHT))) != 0):
                self.state = 1236
                localctx.t = self.join_type()


            self.state = 1239
            self.match(SQLParser.JOIN)
            self.state = 1240
            localctx.r = self.table_primary()
            self.state = 1241
            localctx.s = self.join_specification()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Natural_joinContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Natural_joinContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t = None # Join_typeContext
            self.r = None # Table_primaryContext

        def NATURAL(self):
            return self.getToken(SQLParser.NATURAL, 0)

        def JOIN(self):
            return self.getToken(SQLParser.JOIN, 0)

        def table_primary(self):
            return self.getTypedRuleContext(SQLParser.Table_primaryContext,0)


        def join_type(self):
            return self.getTypedRuleContext(SQLParser.Join_typeContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_natural_join

        def accept(self, visitor):
            if hasattr(visitor, "visitNatural_join"):
                return visitor.visitNatural_join(self)
            else:
                return visitor.visitChildren(self)




    def natural_join(self):

        localctx = SQLParser.Natural_joinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_natural_join)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1243
            self.match(SQLParser.NATURAL)
            self.state = 1245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SQLParser.FULL) | (1 << SQLParser.INNER) | (1 << SQLParser.LEFT) | (1 << SQLParser.RIGHT))) != 0):
                self.state = 1244
                localctx.t = self.join_type()


            self.state = 1247
            self.match(SQLParser.JOIN)
            self.state = 1248
            localctx.r = self.table_primary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Union_joinContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Union_joinContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.r = None # Table_primaryContext

        def UNION(self):
            return self.getToken(SQLParser.UNION, 0)

        def JOIN(self):
            return self.getToken(SQLParser.JOIN, 0)

        def table_primary(self):
            return self.getTypedRuleContext(SQLParser.Table_primaryContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_union_join

        def accept(self, visitor):
            if hasattr(visitor, "visitUnion_join"):
                return visitor.visitUnion_join(self)
            else:
                return visitor.visitChildren(self)




    def union_join(self):

        localctx = SQLParser.Union_joinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_union_join)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1250
            self.match(SQLParser.UNION)
            self.state = 1251
            self.match(SQLParser.JOIN)
            self.state = 1252
            localctx.r = self.table_primary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Join_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Join_typeContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.t = None # Outer_join_typeContext

        def INNER(self):
            return self.getToken(SQLParser.INNER, 0)

        def outer_join_type(self):
            return self.getTypedRuleContext(SQLParser.Outer_join_typeContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_join_type

        def accept(self, visitor):
            if hasattr(visitor, "visitJoin_type"):
                return visitor.visitJoin_type(self)
            else:
                return visitor.visitChildren(self)




    def join_type(self):

        localctx = SQLParser.Join_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_join_type)
        try:
            self.state = 1256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.INNER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1254
                self.match(SQLParser.INNER)
                pass
            elif token in [SQLParser.FULL, SQLParser.LEFT, SQLParser.RIGHT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1255
                localctx.t = self.outer_join_type()
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

    class Outer_join_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Outer_join_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def outer_join_type_part2(self):
            return self.getTypedRuleContext(SQLParser.Outer_join_type_part2Context,0)


        def OUTER(self):
            return self.getToken(SQLParser.OUTER, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_outer_join_type

        def accept(self, visitor):
            if hasattr(visitor, "visitOuter_join_type"):
                return visitor.visitOuter_join_type(self)
            else:
                return visitor.visitChildren(self)




    def outer_join_type(self):

        localctx = SQLParser.Outer_join_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_outer_join_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1258
            self.outer_join_type_part2()
            self.state = 1260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.OUTER:
                self.state = 1259
                self.match(SQLParser.OUTER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Outer_join_type_part2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Outer_join_type_part2Context, self).__init__(parent, invokingState)
            self.parser = parser

        def LEFT(self):
            return self.getToken(SQLParser.LEFT, 0)

        def RIGHT(self):
            return self.getToken(SQLParser.RIGHT, 0)

        def FULL(self):
            return self.getToken(SQLParser.FULL, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_outer_join_type_part2

        def accept(self, visitor):
            if hasattr(visitor, "visitOuter_join_type_part2"):
                return visitor.visitOuter_join_type_part2(self)
            else:
                return visitor.visitChildren(self)




    def outer_join_type_part2(self):

        localctx = SQLParser.Outer_join_type_part2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_outer_join_type_part2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1262
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SQLParser.FULL) | (1 << SQLParser.LEFT) | (1 << SQLParser.RIGHT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Join_specificationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Join_specificationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def join_condition(self):
            return self.getTypedRuleContext(SQLParser.Join_conditionContext,0)


        def named_columns_join(self):
            return self.getTypedRuleContext(SQLParser.Named_columns_joinContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_join_specification

        def accept(self, visitor):
            if hasattr(visitor, "visitJoin_specification"):
                return visitor.visitJoin_specification(self)
            else:
                return visitor.visitChildren(self)




    def join_specification(self):

        localctx = SQLParser.Join_specificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_join_specification)
        try:
            self.state = 1266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.ON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1264
                self.join_condition()
                pass
            elif token in [SQLParser.USING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1265
                self.named_columns_join()
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

    class Join_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Join_conditionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ON(self):
            return self.getToken(SQLParser.ON, 0)

        def search_condition(self):
            return self.getTypedRuleContext(SQLParser.Search_conditionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_join_condition

        def accept(self, visitor):
            if hasattr(visitor, "visitJoin_condition"):
                return visitor.visitJoin_condition(self)
            else:
                return visitor.visitChildren(self)




    def join_condition(self):

        localctx = SQLParser.Join_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_join_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1268
            self.match(SQLParser.ON)
            self.state = 1269
            self.search_condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Named_columns_joinContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Named_columns_joinContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.f = None # Column_reference_listContext

        def USING(self):
            return self.getToken(SQLParser.USING, 0)

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def column_reference_list(self):
            return self.getTypedRuleContext(SQLParser.Column_reference_listContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_named_columns_join

        def accept(self, visitor):
            if hasattr(visitor, "visitNamed_columns_join"):
                return visitor.visitNamed_columns_join(self)
            else:
                return visitor.visitChildren(self)




    def named_columns_join(self):

        localctx = SQLParser.Named_columns_joinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_named_columns_join)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1271
            self.match(SQLParser.USING)
            self.state = 1272
            self.match(SQLParser.LEFT_PAREN)
            self.state = 1273
            localctx.f = self.column_reference_list()
            self.state = 1274
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Table_primaryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Table_primaryContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.alias = None # IdentifierContext
            self.name = None # IdentifierContext

        def table_or_query_name(self):
            return self.getTypedRuleContext(SQLParser.Table_or_query_nameContext,0)


        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def column_name_list(self):
            return self.getTypedRuleContext(SQLParser.Column_name_listContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def AS(self):
            return self.getToken(SQLParser.AS, 0)

        def derived_table(self):
            return self.getTypedRuleContext(SQLParser.Derived_tableContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_table_primary

        def accept(self, visitor):
            if hasattr(visitor, "visitTable_primary"):
                return visitor.visitTable_primary(self)
            else:
                return visitor.visitChildren(self)




    def table_primary(self):

        localctx = SQLParser.Table_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_table_primary)
        self._la = 0 # Token type
        try:
            self.state = 1300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.AVG, SQLParser.BETWEEN, SQLParser.BY, SQLParser.CENTURY, SQLParser.CHARACTER, SQLParser.COLLECT, SQLParser.COALESCE, SQLParser.COLUMN, SQLParser.COUNT, SQLParser.CUBE, SQLParser.DAY, SQLParser.DEC, SQLParser.DECADE, SQLParser.DOW, SQLParser.DOY, SQLParser.DROP, SQLParser.EPOCH, SQLParser.EVERY, SQLParser.EXISTS, SQLParser.EXTERNAL, SQLParser.EXTRACT, SQLParser.FILTER, SQLParser.FIRST, SQLParser.FORMAT, SQLParser.FUSION, SQLParser.GROUPING, SQLParser.HASH, SQLParser.INDEX, SQLParser.INSERT, SQLParser.INTERSECTION, SQLParser.ISODOW, SQLParser.ISOYEAR, SQLParser.LAST, SQLParser.LESS, SQLParser.LIST, SQLParser.LOCATION, SQLParser.MAX, SQLParser.MAXVALUE, SQLParser.MICROSECONDS, SQLParser.MILLENNIUM, SQLParser.MILLISECONDS, SQLParser.MIN, SQLParser.MINUTE, SQLParser.MONTH, SQLParser.NATIONAL, SQLParser.NULLIF, SQLParser.OVERWRITE, SQLParser.PARTITION, SQLParser.PARTITIONS, SQLParser.PRECISION, SQLParser.PURGE, SQLParser.QUARTER, SQLParser.RANGE, SQLParser.REGEXP, SQLParser.RLIKE, SQLParser.ROLLUP, SQLParser.SECOND, SQLParser.SET, SQLParser.SIMILAR, SQLParser.STDDEV_POP, SQLParser.STDDEV_SAMP, SQLParser.SUBPARTITION, SQLParser.SUM, SQLParser.TABLESPACE, SQLParser.THAN, SQLParser.TIMEZONE, SQLParser.TIMEZONE_HOUR, SQLParser.TIMEZONE_MINUTE, SQLParser.TRIM, SQLParser.TO, SQLParser.UNKNOWN, SQLParser.VALUES, SQLParser.VAR_SAMP, SQLParser.VAR_POP, SQLParser.VARYING, SQLParser.WEEK, SQLParser.YEAR, SQLParser.ZONE, SQLParser.BOOLEAN, SQLParser.BOOL, SQLParser.BIT, SQLParser.VARBIT, SQLParser.INT1, SQLParser.INT2, SQLParser.INT4, SQLParser.INT8, SQLParser.TINYINT, SQLParser.SMALLINT, SQLParser.INT, SQLParser.INTEGER, SQLParser.BIGINT, SQLParser.FLOAT4, SQLParser.FLOAT8, SQLParser.REAL, SQLParser.FLOAT, SQLParser.DOUBLE, SQLParser.NUMERIC, SQLParser.DECIMAL, SQLParser.CHAR, SQLParser.VARCHAR, SQLParser.NCHAR, SQLParser.NVARCHAR, SQLParser.DATE, SQLParser.TIME, SQLParser.TIMETZ, SQLParser.TIMESTAMP, SQLParser.TIMESTAMPTZ, SQLParser.TEXT, SQLParser.VARBINARY, SQLParser.BLOB, SQLParser.BYTEA, SQLParser.INET4, SQLParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1276
                self.table_or_query_name()
                self.state = 1281
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SQLParser.AS) | (1 << SQLParser.AVG) | (1 << SQLParser.BETWEEN) | (1 << SQLParser.BY) | (1 << SQLParser.CENTURY) | (1 << SQLParser.CHARACTER) | (1 << SQLParser.COLLECT) | (1 << SQLParser.COALESCE) | (1 << SQLParser.COLUMN) | (1 << SQLParser.COUNT) | (1 << SQLParser.CUBE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (SQLParser.DAY - 64)) | (1 << (SQLParser.DEC - 64)) | (1 << (SQLParser.DECADE - 64)) | (1 << (SQLParser.DOW - 64)) | (1 << (SQLParser.DOY - 64)) | (1 << (SQLParser.DROP - 64)) | (1 << (SQLParser.EPOCH - 64)) | (1 << (SQLParser.EVERY - 64)) | (1 << (SQLParser.EXISTS - 64)) | (1 << (SQLParser.EXTERNAL - 64)) | (1 << (SQLParser.EXTRACT - 64)) | (1 << (SQLParser.FILTER - 64)) | (1 << (SQLParser.FIRST - 64)) | (1 << (SQLParser.FORMAT - 64)) | (1 << (SQLParser.FUSION - 64)) | (1 << (SQLParser.GROUPING - 64)) | (1 << (SQLParser.HASH - 64)) | (1 << (SQLParser.INDEX - 64)) | (1 << (SQLParser.INSERT - 64)) | (1 << (SQLParser.INTERSECTION - 64)) | (1 << (SQLParser.ISODOW - 64)) | (1 << (SQLParser.ISOYEAR - 64)) | (1 << (SQLParser.LAST - 64)) | (1 << (SQLParser.LESS - 64)) | (1 << (SQLParser.LIST - 64)) | (1 << (SQLParser.LOCATION - 64)) | (1 << (SQLParser.MAX - 64)) | (1 << (SQLParser.MAXVALUE - 64)) | (1 << (SQLParser.MICROSECONDS - 64)) | (1 << (SQLParser.MILLENNIUM - 64)) | (1 << (SQLParser.MILLISECONDS - 64)) | (1 << (SQLParser.MIN - 64)) | (1 << (SQLParser.MINUTE - 64)) | (1 << (SQLParser.MONTH - 64)) | (1 << (SQLParser.NATIONAL - 64)) | (1 << (SQLParser.NULLIF - 64)) | (1 << (SQLParser.OVERWRITE - 64)) | (1 << (SQLParser.PARTITION - 64)) | (1 << (SQLParser.PARTITIONS - 64)) | (1 << (SQLParser.PRECISION - 64)) | (1 << (SQLParser.PURGE - 64)) | (1 << (SQLParser.QUARTER - 64)) | (1 << (SQLParser.RANGE - 64)) | (1 << (SQLParser.REGEXP - 64)) | (1 << (SQLParser.RLIKE - 64)) | (1 << (SQLParser.ROLLUP - 64)) | (1 << (SQLParser.SECOND - 64)) | (1 << (SQLParser.SET - 64)) | (1 << (SQLParser.SIMILAR - 64)) | (1 << (SQLParser.STDDEV_POP - 64)) | (1 << (SQLParser.STDDEV_SAMP - 64)) | (1 << (SQLParser.SUBPARTITION - 64)) | (1 << (SQLParser.SUM - 64)) | (1 << (SQLParser.TABLESPACE - 64)) | (1 << (SQLParser.THAN - 64)) | (1 << (SQLParser.TIMEZONE - 64)) | (1 << (SQLParser.TIMEZONE_HOUR - 64)) | (1 << (SQLParser.TIMEZONE_MINUTE - 64)) | (1 << (SQLParser.TRIM - 64)) | (1 << (SQLParser.TO - 64)) | (1 << (SQLParser.UNKNOWN - 64)) | (1 << (SQLParser.VALUES - 64)) | (1 << (SQLParser.VAR_SAMP - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (SQLParser.VAR_POP - 128)) | (1 << (SQLParser.VARYING - 128)) | (1 << (SQLParser.WEEK - 128)) | (1 << (SQLParser.YEAR - 128)) | (1 << (SQLParser.ZONE - 128)) | (1 << (SQLParser.BOOLEAN - 128)) | (1 << (SQLParser.BOOL - 128)) | (1 << (SQLParser.BIT - 128)) | (1 << (SQLParser.VARBIT - 128)) | (1 << (SQLParser.INT1 - 128)) | (1 << (SQLParser.INT2 - 128)) | (1 << (SQLParser.INT4 - 128)) | (1 << (SQLParser.INT8 - 128)) | (1 << (SQLParser.TINYINT - 128)) | (1 << (SQLParser.SMALLINT - 128)) | (1 << (SQLParser.INT - 128)) | (1 << (SQLParser.INTEGER - 128)) | (1 << (SQLParser.BIGINT - 128)) | (1 << (SQLParser.FLOAT4 - 128)) | (1 << (SQLParser.FLOAT8 - 128)) | (1 << (SQLParser.REAL - 128)) | (1 << (SQLParser.FLOAT - 128)) | (1 << (SQLParser.DOUBLE - 128)) | (1 << (SQLParser.NUMERIC - 128)) | (1 << (SQLParser.DECIMAL - 128)) | (1 << (SQLParser.CHAR - 128)) | (1 << (SQLParser.VARCHAR - 128)) | (1 << (SQLParser.NCHAR - 128)) | (1 << (SQLParser.NVARCHAR - 128)) | (1 << (SQLParser.DATE - 128)) | (1 << (SQLParser.TIME - 128)) | (1 << (SQLParser.TIMETZ - 128)) | (1 << (SQLParser.TIMESTAMP - 128)) | (1 << (SQLParser.TIMESTAMPTZ - 128)) | (1 << (SQLParser.TEXT - 128)) | (1 << (SQLParser.VARBINARY - 128)) | (1 << (SQLParser.BLOB - 128)) | (1 << (SQLParser.BYTEA - 128)) | (1 << (SQLParser.INET4 - 128)))) != 0) or _la==SQLParser.Identifier:
                    self.state = 1278
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==SQLParser.AS:
                        self.state = 1277
                        self.match(SQLParser.AS)


                    self.state = 1280
                    localctx.alias = self.identifier()


                self.state = 1287
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 1283
                    self.match(SQLParser.LEFT_PAREN)
                    self.state = 1284
                    self.column_name_list()
                    self.state = 1285
                    self.match(SQLParser.RIGHT_PAREN)


                pass
            elif token in [SQLParser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1289
                self.derived_table()
                self.state = 1291
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.AS:
                    self.state = 1290
                    self.match(SQLParser.AS)


                self.state = 1293
                localctx.name = self.identifier()
                self.state = 1298
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.LEFT_PAREN:
                    self.state = 1294
                    self.match(SQLParser.LEFT_PAREN)
                    self.state = 1295
                    self.column_name_list()
                    self.state = 1296
                    self.match(SQLParser.RIGHT_PAREN)


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

    class Column_name_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Column_name_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(SQLParser.IdentifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_column_name_list

        def accept(self, visitor):
            if hasattr(visitor, "visitColumn_name_list"):
                return visitor.visitColumn_name_list(self)
            else:
                return visitor.visitChildren(self)




    def column_name_list(self):

        localctx = SQLParser.Column_name_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_column_name_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1302
            self.identifier()
            self.state = 1307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.COMMA:
                self.state = 1303
                self.match(SQLParser.COMMA)
                self.state = 1304
                self.identifier()
                self.state = 1309
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Derived_tableContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Derived_tableContext, self).__init__(parent, invokingState)
            self.parser = parser

        def table_subquery(self):
            return self.getTypedRuleContext(SQLParser.Table_subqueryContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_derived_table

        def accept(self, visitor):
            if hasattr(visitor, "visitDerived_table"):
                return visitor.visitDerived_table(self)
            else:
                return visitor.visitChildren(self)




    def derived_table(self):

        localctx = SQLParser.Derived_tableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_derived_table)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1310
            self.table_subquery()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Where_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Where_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(SQLParser.WHERE, 0)

        def search_condition(self):
            return self.getTypedRuleContext(SQLParser.Search_conditionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_where_clause

        def accept(self, visitor):
            if hasattr(visitor, "visitWhere_clause"):
                return visitor.visitWhere_clause(self)
            else:
                return visitor.visitChildren(self)




    def where_clause(self):

        localctx = SQLParser.Where_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_where_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1312
            self.match(SQLParser.WHERE)
            self.state = 1313
            self.search_condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Search_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Search_conditionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def value_expression(self):
            return self.getTypedRuleContext(SQLParser.Value_expressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_search_condition

        def accept(self, visitor):
            if hasattr(visitor, "visitSearch_condition"):
                return visitor.visitSearch_condition(self)
            else:
                return visitor.visitChildren(self)




    def search_condition(self):

        localctx = SQLParser.Search_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_search_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1315
            self.value_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Groupby_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Groupby_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.g = None # Grouping_element_listContext

        def GROUP(self):
            return self.getToken(SQLParser.GROUP, 0)

        def BY(self):
            return self.getToken(SQLParser.BY, 0)

        def grouping_element_list(self):
            return self.getTypedRuleContext(SQLParser.Grouping_element_listContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_groupby_clause

        def accept(self, visitor):
            if hasattr(visitor, "visitGroupby_clause"):
                return visitor.visitGroupby_clause(self)
            else:
                return visitor.visitChildren(self)




    def groupby_clause(self):

        localctx = SQLParser.Groupby_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_groupby_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1317
            self.match(SQLParser.GROUP)
            self.state = 1318
            self.match(SQLParser.BY)
            self.state = 1319
            localctx.g = self.grouping_element_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Grouping_element_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Grouping_element_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def grouping_element(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Grouping_elementContext)
            else:
                return self.getTypedRuleContext(SQLParser.Grouping_elementContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_grouping_element_list

        def accept(self, visitor):
            if hasattr(visitor, "visitGrouping_element_list"):
                return visitor.visitGrouping_element_list(self)
            else:
                return visitor.visitChildren(self)




    def grouping_element_list(self):

        localctx = SQLParser.Grouping_element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_grouping_element_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1321
            self.grouping_element()
            self.state = 1326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.COMMA:
                self.state = 1322
                self.match(SQLParser.COMMA)
                self.state = 1323
                self.grouping_element()
                self.state = 1328
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Grouping_elementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Grouping_elementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def rollup_list(self):
            return self.getTypedRuleContext(SQLParser.Rollup_listContext,0)


        def cube_list(self):
            return self.getTypedRuleContext(SQLParser.Cube_listContext,0)


        def empty_grouping_set(self):
            return self.getTypedRuleContext(SQLParser.Empty_grouping_setContext,0)


        def ordinary_grouping_set(self):
            return self.getTypedRuleContext(SQLParser.Ordinary_grouping_setContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_grouping_element

        def accept(self, visitor):
            if hasattr(visitor, "visitGrouping_element"):
                return visitor.visitGrouping_element(self)
            else:
                return visitor.visitChildren(self)




    def grouping_element(self):

        localctx = SQLParser.Grouping_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_grouping_element)
        try:
            self.state = 1333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,131,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1329
                self.rollup_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1330
                self.cube_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1331
                self.empty_grouping_set()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1332
                self.ordinary_grouping_set()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Ordinary_grouping_setContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Ordinary_grouping_setContext, self).__init__(parent, invokingState)
            self.parser = parser

        def row_value_predicand(self):
            return self.getTypedRuleContext(SQLParser.Row_value_predicandContext,0)


        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def row_value_predicand_list(self):
            return self.getTypedRuleContext(SQLParser.Row_value_predicand_listContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_ordinary_grouping_set

        def accept(self, visitor):
            if hasattr(visitor, "visitOrdinary_grouping_set"):
                return visitor.visitOrdinary_grouping_set(self)
            else:
                return visitor.visitChildren(self)




    def ordinary_grouping_set(self):

        localctx = SQLParser.Ordinary_grouping_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_ordinary_grouping_set)
        try:
            self.state = 1340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,132,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1335
                self.row_value_predicand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1336
                self.match(SQLParser.LEFT_PAREN)
                self.state = 1337
                self.row_value_predicand_list()
                self.state = 1338
                self.match(SQLParser.RIGHT_PAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Ordinary_grouping_set_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Ordinary_grouping_set_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ordinary_grouping_set(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Ordinary_grouping_setContext)
            else:
                return self.getTypedRuleContext(SQLParser.Ordinary_grouping_setContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_ordinary_grouping_set_list

        def accept(self, visitor):
            if hasattr(visitor, "visitOrdinary_grouping_set_list"):
                return visitor.visitOrdinary_grouping_set_list(self)
            else:
                return visitor.visitChildren(self)




    def ordinary_grouping_set_list(self):

        localctx = SQLParser.Ordinary_grouping_set_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_ordinary_grouping_set_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1342
            self.ordinary_grouping_set()
            self.state = 1347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.COMMA:
                self.state = 1343
                self.match(SQLParser.COMMA)
                self.state = 1344
                self.ordinary_grouping_set()
                self.state = 1349
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Rollup_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Rollup_listContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.c = None # Ordinary_grouping_set_listContext

        def ROLLUP(self):
            return self.getToken(SQLParser.ROLLUP, 0)

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def ordinary_grouping_set_list(self):
            return self.getTypedRuleContext(SQLParser.Ordinary_grouping_set_listContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_rollup_list

        def accept(self, visitor):
            if hasattr(visitor, "visitRollup_list"):
                return visitor.visitRollup_list(self)
            else:
                return visitor.visitChildren(self)




    def rollup_list(self):

        localctx = SQLParser.Rollup_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_rollup_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1350
            self.match(SQLParser.ROLLUP)
            self.state = 1351
            self.match(SQLParser.LEFT_PAREN)
            self.state = 1352
            localctx.c = self.ordinary_grouping_set_list()
            self.state = 1353
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Cube_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Cube_listContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.c = None # Ordinary_grouping_set_listContext

        def CUBE(self):
            return self.getToken(SQLParser.CUBE, 0)

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def ordinary_grouping_set_list(self):
            return self.getTypedRuleContext(SQLParser.Ordinary_grouping_set_listContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_cube_list

        def accept(self, visitor):
            if hasattr(visitor, "visitCube_list"):
                return visitor.visitCube_list(self)
            else:
                return visitor.visitChildren(self)




    def cube_list(self):

        localctx = SQLParser.Cube_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_cube_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1355
            self.match(SQLParser.CUBE)
            self.state = 1356
            self.match(SQLParser.LEFT_PAREN)
            self.state = 1357
            localctx.c = self.ordinary_grouping_set_list()
            self.state = 1358
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Empty_grouping_setContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Empty_grouping_setContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_empty_grouping_set

        def accept(self, visitor):
            if hasattr(visitor, "visitEmpty_grouping_set"):
                return visitor.visitEmpty_grouping_set(self)
            else:
                return visitor.visitChildren(self)




    def empty_grouping_set(self):

        localctx = SQLParser.Empty_grouping_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_empty_grouping_set)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1360
            self.match(SQLParser.LEFT_PAREN)
            self.state = 1361
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Having_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Having_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def HAVING(self):
            return self.getToken(SQLParser.HAVING, 0)

        def boolean_value_expression(self):
            return self.getTypedRuleContext(SQLParser.Boolean_value_expressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_having_clause

        def accept(self, visitor):
            if hasattr(visitor, "visitHaving_clause"):
                return visitor.visitHaving_clause(self)
            else:
                return visitor.visitChildren(self)




    def having_clause(self):

        localctx = SQLParser.Having_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_having_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1363
            self.match(SQLParser.HAVING)
            self.state = 1364
            self.boolean_value_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Row_value_predicand_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Row_value_predicand_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def row_value_predicand(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Row_value_predicandContext)
            else:
                return self.getTypedRuleContext(SQLParser.Row_value_predicandContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_row_value_predicand_list

        def accept(self, visitor):
            if hasattr(visitor, "visitRow_value_predicand_list"):
                return visitor.visitRow_value_predicand_list(self)
            else:
                return visitor.visitChildren(self)




    def row_value_predicand_list(self):

        localctx = SQLParser.Row_value_predicand_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_row_value_predicand_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1366
            self.row_value_predicand()
            self.state = 1371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.COMMA:
                self.state = 1367
                self.match(SQLParser.COMMA)
                self.state = 1368
                self.row_value_predicand()
                self.state = 1373
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Query_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Query_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def query_expression_body(self):
            return self.getTypedRuleContext(SQLParser.Query_expression_bodyContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_query_expression

        def accept(self, visitor):
            if hasattr(visitor, "visitQuery_expression"):
                return visitor.visitQuery_expression(self)
            else:
                return visitor.visitChildren(self)




    def query_expression(self):

        localctx = SQLParser.Query_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_query_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1374
            self.query_expression_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Query_expression_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Query_expression_bodyContext, self).__init__(parent, invokingState)
            self.parser = parser

        def non_join_query_expression(self):
            return self.getTypedRuleContext(SQLParser.Non_join_query_expressionContext,0)


        def joined_table(self):
            return self.getTypedRuleContext(SQLParser.Joined_tableContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_query_expression_body

        def accept(self, visitor):
            if hasattr(visitor, "visitQuery_expression_body"):
                return visitor.visitQuery_expression_body(self)
            else:
                return visitor.visitChildren(self)




    def query_expression_body(self):

        localctx = SQLParser.Query_expression_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_query_expression_body)
        try:
            self.state = 1378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,135,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1376
                self.non_join_query_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1377
                self.joined_table()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Non_join_query_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Non_join_query_expressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def non_join_query_term(self):
            return self.getTypedRuleContext(SQLParser.Non_join_query_termContext,0)


        def joined_table(self):
            return self.getTypedRuleContext(SQLParser.Joined_tableContext,0)


        def query_term(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Query_termContext)
            else:
                return self.getTypedRuleContext(SQLParser.Query_termContext,i)


        def UNION(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.UNION)
            else:
                return self.getToken(SQLParser.UNION, i)

        def EXCEPT(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.EXCEPT)
            else:
                return self.getToken(SQLParser.EXCEPT, i)

        def ALL(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.ALL)
            else:
                return self.getToken(SQLParser.ALL, i)

        def DISTINCT(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.DISTINCT)
            else:
                return self.getToken(SQLParser.DISTINCT, i)

        def getRuleIndex(self):
            return SQLParser.RULE_non_join_query_expression

        def accept(self, visitor):
            if hasattr(visitor, "visitNon_join_query_expression"):
                return visitor.visitNon_join_query_expression(self)
            else:
                return visitor.visitChildren(self)




    def non_join_query_expression(self):

        localctx = SQLParser.Non_join_query_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_non_join_query_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,137,self._ctx)
            if la_ == 1:
                self.state = 1380
                self.non_join_query_term()
                pass

            elif la_ == 2:
                self.state = 1381
                self.joined_table()
                self.state = 1382
                _la = self._input.LA(1)
                if not(_la==SQLParser.EXCEPT or _la==SQLParser.UNION):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 1384
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.ALL or _la==SQLParser.DISTINCT:
                    self.state = 1383
                    _la = self._input.LA(1)
                    if not(_la==SQLParser.ALL or _la==SQLParser.DISTINCT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 1386
                self.query_term()
                pass


            self.state = 1397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.EXCEPT or _la==SQLParser.UNION:
                self.state = 1390
                _la = self._input.LA(1)
                if not(_la==SQLParser.EXCEPT or _la==SQLParser.UNION):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 1392
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.ALL or _la==SQLParser.DISTINCT:
                    self.state = 1391
                    _la = self._input.LA(1)
                    if not(_la==SQLParser.ALL or _la==SQLParser.DISTINCT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 1394
                self.query_term()
                self.state = 1399
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Query_termContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Query_termContext, self).__init__(parent, invokingState)
            self.parser = parser

        def non_join_query_term(self):
            return self.getTypedRuleContext(SQLParser.Non_join_query_termContext,0)


        def joined_table(self):
            return self.getTypedRuleContext(SQLParser.Joined_tableContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_query_term

        def accept(self, visitor):
            if hasattr(visitor, "visitQuery_term"):
                return visitor.visitQuery_term(self)
            else:
                return visitor.visitChildren(self)




    def query_term(self):

        localctx = SQLParser.Query_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_query_term)
        try:
            self.state = 1402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,140,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1400
                self.non_join_query_term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1401
                self.joined_table()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Non_join_query_termContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Non_join_query_termContext, self).__init__(parent, invokingState)
            self.parser = parser

        def non_join_query_primary(self):
            return self.getTypedRuleContext(SQLParser.Non_join_query_primaryContext,0)


        def joined_table(self):
            return self.getTypedRuleContext(SQLParser.Joined_tableContext,0)


        def INTERSECT(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.INTERSECT)
            else:
                return self.getToken(SQLParser.INTERSECT, i)

        def query_primary(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Query_primaryContext)
            else:
                return self.getTypedRuleContext(SQLParser.Query_primaryContext,i)


        def ALL(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.ALL)
            else:
                return self.getToken(SQLParser.ALL, i)

        def DISTINCT(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.DISTINCT)
            else:
                return self.getToken(SQLParser.DISTINCT, i)

        def getRuleIndex(self):
            return SQLParser.RULE_non_join_query_term

        def accept(self, visitor):
            if hasattr(visitor, "visitNon_join_query_term"):
                return visitor.visitNon_join_query_term(self)
            else:
                return visitor.visitChildren(self)




    def non_join_query_term(self):

        localctx = SQLParser.Non_join_query_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_non_join_query_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,142,self._ctx)
            if la_ == 1:
                self.state = 1404
                self.non_join_query_primary()
                pass

            elif la_ == 2:
                self.state = 1405
                self.joined_table()
                self.state = 1406
                self.match(SQLParser.INTERSECT)
                self.state = 1408
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.ALL or _la==SQLParser.DISTINCT:
                    self.state = 1407
                    _la = self._input.LA(1)
                    if not(_la==SQLParser.ALL or _la==SQLParser.DISTINCT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 1410
                self.query_primary()
                pass


            self.state = 1421
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.INTERSECT:
                self.state = 1414
                self.match(SQLParser.INTERSECT)
                self.state = 1416
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.ALL or _la==SQLParser.DISTINCT:
                    self.state = 1415
                    _la = self._input.LA(1)
                    if not(_la==SQLParser.ALL or _la==SQLParser.DISTINCT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 1418
                self.query_primary()
                self.state = 1423
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Query_primaryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Query_primaryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def non_join_query_primary(self):
            return self.getTypedRuleContext(SQLParser.Non_join_query_primaryContext,0)


        def joined_table(self):
            return self.getTypedRuleContext(SQLParser.Joined_tableContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_query_primary

        def accept(self, visitor):
            if hasattr(visitor, "visitQuery_primary"):
                return visitor.visitQuery_primary(self)
            else:
                return visitor.visitChildren(self)




    def query_primary(self):

        localctx = SQLParser.Query_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_query_primary)
        try:
            self.state = 1426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,145,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1424
                self.non_join_query_primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1425
                self.joined_table()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Non_join_query_primaryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Non_join_query_primaryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def simple_table(self):
            return self.getTypedRuleContext(SQLParser.Simple_tableContext,0)


        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def non_join_query_expression(self):
            return self.getTypedRuleContext(SQLParser.Non_join_query_expressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_non_join_query_primary

        def accept(self, visitor):
            if hasattr(visitor, "visitNon_join_query_primary"):
                return visitor.visitNon_join_query_primary(self)
            else:
                return visitor.visitChildren(self)




    def non_join_query_primary(self):

        localctx = SQLParser.Non_join_query_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_non_join_query_primary)
        try:
            self.state = 1433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.SELECT, SQLParser.TABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1428
                self.simple_table()
                pass
            elif token in [SQLParser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1429
                self.match(SQLParser.LEFT_PAREN)
                self.state = 1430
                self.non_join_query_expression()
                self.state = 1431
                self.match(SQLParser.RIGHT_PAREN)
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

    class Simple_tableContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Simple_tableContext, self).__init__(parent, invokingState)
            self.parser = parser

        def query_specification(self):
            return self.getTypedRuleContext(SQLParser.Query_specificationContext,0)


        def explicit_table(self):
            return self.getTypedRuleContext(SQLParser.Explicit_tableContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_simple_table

        def accept(self, visitor):
            if hasattr(visitor, "visitSimple_table"):
                return visitor.visitSimple_table(self)
            else:
                return visitor.visitChildren(self)




    def simple_table(self):

        localctx = SQLParser.Simple_tableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_simple_table)
        try:
            self.state = 1437
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.SELECT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1435
                self.query_specification()
                pass
            elif token in [SQLParser.TABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1436
                self.explicit_table()
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

    class Explicit_tableContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Explicit_tableContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TABLE(self):
            return self.getToken(SQLParser.TABLE, 0)

        def table_or_query_name(self):
            return self.getTypedRuleContext(SQLParser.Table_or_query_nameContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_explicit_table

        def accept(self, visitor):
            if hasattr(visitor, "visitExplicit_table"):
                return visitor.visitExplicit_table(self)
            else:
                return visitor.visitChildren(self)




    def explicit_table(self):

        localctx = SQLParser.Explicit_tableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_explicit_table)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1439
            self.match(SQLParser.TABLE)
            self.state = 1440
            self.table_or_query_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Table_or_query_nameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Table_or_query_nameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def table_name(self):
            return self.getTypedRuleContext(SQLParser.Table_nameContext,0)


        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_table_or_query_name

        def accept(self, visitor):
            if hasattr(visitor, "visitTable_or_query_name"):
                return visitor.visitTable_or_query_name(self)
            else:
                return visitor.visitChildren(self)




    def table_or_query_name(self):

        localctx = SQLParser.Table_or_query_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_table_or_query_name)
        try:
            self.state = 1444
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,148,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1442
                self.table_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1443
                self.identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Table_nameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Table_nameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(SQLParser.IdentifierContext,i)


        def DOT(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.DOT)
            else:
                return self.getToken(SQLParser.DOT, i)

        def getRuleIndex(self):
            return SQLParser.RULE_table_name

        def accept(self, visitor):
            if hasattr(visitor, "visitTable_name"):
                return visitor.visitTable_name(self)
            else:
                return visitor.visitChildren(self)




    def table_name(self):

        localctx = SQLParser.Table_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_table_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1446
            self.identifier()
            self.state = 1453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.DOT:
                self.state = 1447
                self.match(SQLParser.DOT)
                self.state = 1448
                self.identifier()
                self.state = 1451
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.DOT:
                    self.state = 1449
                    self.match(SQLParser.DOT)
                    self.state = 1450
                    self.identifier()




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Query_specificationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Query_specificationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(SQLParser.SELECT, 0)

        def select_list(self):
            return self.getTypedRuleContext(SQLParser.Select_listContext,0)


        def set_qualifier(self):
            return self.getTypedRuleContext(SQLParser.Set_qualifierContext,0)


        def table_expression(self):
            return self.getTypedRuleContext(SQLParser.Table_expressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_query_specification

        def accept(self, visitor):
            if hasattr(visitor, "visitQuery_specification"):
                return visitor.visitQuery_specification(self)
            else:
                return visitor.visitChildren(self)




    def query_specification(self):

        localctx = SQLParser.Query_specificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_query_specification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1455
            self.match(SQLParser.SELECT)
            self.state = 1457
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.ALL or _la==SQLParser.DISTINCT:
                self.state = 1456
                self.set_qualifier()


            self.state = 1459
            self.select_list()
            self.state = 1461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.FROM:
                self.state = 1460
                self.table_expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Select_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Select_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def select_sublist(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Select_sublistContext)
            else:
                return self.getTypedRuleContext(SQLParser.Select_sublistContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_select_list

        def accept(self, visitor):
            if hasattr(visitor, "visitSelect_list"):
                return visitor.visitSelect_list(self)
            else:
                return visitor.visitChildren(self)




    def select_list(self):

        localctx = SQLParser.Select_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_select_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1463
            self.select_sublist()
            self.state = 1468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.COMMA:
                self.state = 1464
                self.match(SQLParser.COMMA)
                self.state = 1465
                self.select_sublist()
                self.state = 1470
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Select_sublistContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Select_sublistContext, self).__init__(parent, invokingState)
            self.parser = parser

        def derived_column(self):
            return self.getTypedRuleContext(SQLParser.Derived_columnContext,0)


        def qualified_asterisk(self):
            return self.getTypedRuleContext(SQLParser.Qualified_asteriskContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_select_sublist

        def accept(self, visitor):
            if hasattr(visitor, "visitSelect_sublist"):
                return visitor.visitSelect_sublist(self)
            else:
                return visitor.visitChildren(self)




    def select_sublist(self):

        localctx = SQLParser.Select_sublistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_select_sublist)
        try:
            self.state = 1473
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,154,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1471
                self.derived_column()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1472
                self.qualified_asterisk()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Derived_columnContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Derived_columnContext, self).__init__(parent, invokingState)
            self.parser = parser

        def value_expression(self):
            return self.getTypedRuleContext(SQLParser.Value_expressionContext,0)


        def as_clause(self):
            return self.getTypedRuleContext(SQLParser.As_clauseContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_derived_column

        def accept(self, visitor):
            if hasattr(visitor, "visitDerived_column"):
                return visitor.visitDerived_column(self)
            else:
                return visitor.visitChildren(self)




    def derived_column(self):

        localctx = SQLParser.Derived_columnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_derived_column)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1475
            self.value_expression()
            self.state = 1477
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SQLParser.AS) | (1 << SQLParser.AVG) | (1 << SQLParser.BETWEEN) | (1 << SQLParser.BY) | (1 << SQLParser.CENTURY) | (1 << SQLParser.CHARACTER) | (1 << SQLParser.COLLECT) | (1 << SQLParser.COALESCE) | (1 << SQLParser.COLUMN) | (1 << SQLParser.COUNT) | (1 << SQLParser.CUBE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (SQLParser.DAY - 64)) | (1 << (SQLParser.DEC - 64)) | (1 << (SQLParser.DECADE - 64)) | (1 << (SQLParser.DOW - 64)) | (1 << (SQLParser.DOY - 64)) | (1 << (SQLParser.DROP - 64)) | (1 << (SQLParser.EPOCH - 64)) | (1 << (SQLParser.EVERY - 64)) | (1 << (SQLParser.EXISTS - 64)) | (1 << (SQLParser.EXTERNAL - 64)) | (1 << (SQLParser.EXTRACT - 64)) | (1 << (SQLParser.FILTER - 64)) | (1 << (SQLParser.FIRST - 64)) | (1 << (SQLParser.FORMAT - 64)) | (1 << (SQLParser.FUSION - 64)) | (1 << (SQLParser.GROUPING - 64)) | (1 << (SQLParser.HASH - 64)) | (1 << (SQLParser.INDEX - 64)) | (1 << (SQLParser.INSERT - 64)) | (1 << (SQLParser.INTERSECTION - 64)) | (1 << (SQLParser.ISODOW - 64)) | (1 << (SQLParser.ISOYEAR - 64)) | (1 << (SQLParser.LAST - 64)) | (1 << (SQLParser.LESS - 64)) | (1 << (SQLParser.LIST - 64)) | (1 << (SQLParser.LOCATION - 64)) | (1 << (SQLParser.MAX - 64)) | (1 << (SQLParser.MAXVALUE - 64)) | (1 << (SQLParser.MICROSECONDS - 64)) | (1 << (SQLParser.MILLENNIUM - 64)) | (1 << (SQLParser.MILLISECONDS - 64)) | (1 << (SQLParser.MIN - 64)) | (1 << (SQLParser.MINUTE - 64)) | (1 << (SQLParser.MONTH - 64)) | (1 << (SQLParser.NATIONAL - 64)) | (1 << (SQLParser.NULLIF - 64)) | (1 << (SQLParser.OVERWRITE - 64)) | (1 << (SQLParser.PARTITION - 64)) | (1 << (SQLParser.PARTITIONS - 64)) | (1 << (SQLParser.PRECISION - 64)) | (1 << (SQLParser.PURGE - 64)) | (1 << (SQLParser.QUARTER - 64)) | (1 << (SQLParser.RANGE - 64)) | (1 << (SQLParser.REGEXP - 64)) | (1 << (SQLParser.RLIKE - 64)) | (1 << (SQLParser.ROLLUP - 64)) | (1 << (SQLParser.SECOND - 64)) | (1 << (SQLParser.SET - 64)) | (1 << (SQLParser.SIMILAR - 64)) | (1 << (SQLParser.STDDEV_POP - 64)) | (1 << (SQLParser.STDDEV_SAMP - 64)) | (1 << (SQLParser.SUBPARTITION - 64)) | (1 << (SQLParser.SUM - 64)) | (1 << (SQLParser.TABLESPACE - 64)) | (1 << (SQLParser.THAN - 64)) | (1 << (SQLParser.TIMEZONE - 64)) | (1 << (SQLParser.TIMEZONE_HOUR - 64)) | (1 << (SQLParser.TIMEZONE_MINUTE - 64)) | (1 << (SQLParser.TRIM - 64)) | (1 << (SQLParser.TO - 64)) | (1 << (SQLParser.UNKNOWN - 64)) | (1 << (SQLParser.VALUES - 64)) | (1 << (SQLParser.VAR_SAMP - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (SQLParser.VAR_POP - 128)) | (1 << (SQLParser.VARYING - 128)) | (1 << (SQLParser.WEEK - 128)) | (1 << (SQLParser.YEAR - 128)) | (1 << (SQLParser.ZONE - 128)) | (1 << (SQLParser.BOOLEAN - 128)) | (1 << (SQLParser.BOOL - 128)) | (1 << (SQLParser.BIT - 128)) | (1 << (SQLParser.VARBIT - 128)) | (1 << (SQLParser.INT1 - 128)) | (1 << (SQLParser.INT2 - 128)) | (1 << (SQLParser.INT4 - 128)) | (1 << (SQLParser.INT8 - 128)) | (1 << (SQLParser.TINYINT - 128)) | (1 << (SQLParser.SMALLINT - 128)) | (1 << (SQLParser.INT - 128)) | (1 << (SQLParser.INTEGER - 128)) | (1 << (SQLParser.BIGINT - 128)) | (1 << (SQLParser.FLOAT4 - 128)) | (1 << (SQLParser.FLOAT8 - 128)) | (1 << (SQLParser.REAL - 128)) | (1 << (SQLParser.FLOAT - 128)) | (1 << (SQLParser.DOUBLE - 128)) | (1 << (SQLParser.NUMERIC - 128)) | (1 << (SQLParser.DECIMAL - 128)) | (1 << (SQLParser.CHAR - 128)) | (1 << (SQLParser.VARCHAR - 128)) | (1 << (SQLParser.NCHAR - 128)) | (1 << (SQLParser.NVARCHAR - 128)) | (1 << (SQLParser.DATE - 128)) | (1 << (SQLParser.TIME - 128)) | (1 << (SQLParser.TIMETZ - 128)) | (1 << (SQLParser.TIMESTAMP - 128)) | (1 << (SQLParser.TIMESTAMPTZ - 128)) | (1 << (SQLParser.TEXT - 128)) | (1 << (SQLParser.VARBINARY - 128)) | (1 << (SQLParser.BLOB - 128)) | (1 << (SQLParser.BYTEA - 128)) | (1 << (SQLParser.INET4 - 128)))) != 0) or _la==SQLParser.Identifier:
                self.state = 1476
                self.as_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Qualified_asteriskContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Qualified_asteriskContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.tb_name = None # Token

        def MULTIPLY(self):
            return self.getToken(SQLParser.MULTIPLY, 0)

        def DOT(self):
            return self.getToken(SQLParser.DOT, 0)

        def Identifier(self):
            return self.getToken(SQLParser.Identifier, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_qualified_asterisk

        def accept(self, visitor):
            if hasattr(visitor, "visitQualified_asterisk"):
                return visitor.visitQualified_asterisk(self)
            else:
                return visitor.visitChildren(self)




    def qualified_asterisk(self):

        localctx = SQLParser.Qualified_asteriskContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_qualified_asterisk)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.Identifier:
                self.state = 1479
                localctx.tb_name = self.match(SQLParser.Identifier)
                self.state = 1480
                self.match(SQLParser.DOT)


            self.state = 1483
            self.match(SQLParser.MULTIPLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_qualifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Set_qualifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DISTINCT(self):
            return self.getToken(SQLParser.DISTINCT, 0)

        def ALL(self):
            return self.getToken(SQLParser.ALL, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_set_qualifier

        def accept(self, visitor):
            if hasattr(visitor, "visitSet_qualifier"):
                return visitor.visitSet_qualifier(self)
            else:
                return visitor.visitChildren(self)




    def set_qualifier(self):

        localctx = SQLParser.Set_qualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 320, self.RULE_set_qualifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1485
            _la = self._input.LA(1)
            if not(_la==SQLParser.ALL or _la==SQLParser.DISTINCT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Column_referenceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Column_referenceContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.tb_name = None # IdentifierContext
            self.name = None # IdentifierContext

        def identifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(SQLParser.IdentifierContext,i)


        def DOT(self):
            return self.getToken(SQLParser.DOT, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_column_reference

        def accept(self, visitor):
            if hasattr(visitor, "visitColumn_reference"):
                return visitor.visitColumn_reference(self)
            else:
                return visitor.visitChildren(self)




    def column_reference(self):

        localctx = SQLParser.Column_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_column_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1490
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,157,self._ctx)
            if la_ == 1:
                self.state = 1487
                localctx.tb_name = self.identifier()
                self.state = 1488
                self.match(SQLParser.DOT)


            self.state = 1492
            localctx.name = self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class As_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.As_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def AS(self):
            return self.getToken(SQLParser.AS, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_as_clause

        def accept(self, visitor):
            if hasattr(visitor, "visitAs_clause"):
                return visitor.visitAs_clause(self)
            else:
                return visitor.visitChildren(self)




    def as_clause(self):

        localctx = SQLParser.As_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_as_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1495
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.AS:
                self.state = 1494
                self.match(SQLParser.AS)


            self.state = 1497
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Column_reference_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Column_reference_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def column_reference(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Column_referenceContext)
            else:
                return self.getTypedRuleContext(SQLParser.Column_referenceContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_column_reference_list

        def accept(self, visitor):
            if hasattr(visitor, "visitColumn_reference_list"):
                return visitor.visitColumn_reference_list(self)
            else:
                return visitor.visitChildren(self)




    def column_reference_list(self):

        localctx = SQLParser.Column_reference_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 326, self.RULE_column_reference_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1499
            self.column_reference()
            self.state = 1504
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.COMMA:
                self.state = 1500
                self.match(SQLParser.COMMA)
                self.state = 1501
                self.column_reference()
                self.state = 1506
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Scalar_subqueryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Scalar_subqueryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def subquery(self):
            return self.getTypedRuleContext(SQLParser.SubqueryContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_scalar_subquery

        def accept(self, visitor):
            if hasattr(visitor, "visitScalar_subquery"):
                return visitor.visitScalar_subquery(self)
            else:
                return visitor.visitChildren(self)




    def scalar_subquery(self):

        localctx = SQLParser.Scalar_subqueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_scalar_subquery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1507
            self.subquery()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Row_subqueryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Row_subqueryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def subquery(self):
            return self.getTypedRuleContext(SQLParser.SubqueryContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_row_subquery

        def accept(self, visitor):
            if hasattr(visitor, "visitRow_subquery"):
                return visitor.visitRow_subquery(self)
            else:
                return visitor.visitChildren(self)




    def row_subquery(self):

        localctx = SQLParser.Row_subqueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_row_subquery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1509
            self.subquery()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Table_subqueryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Table_subqueryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def subquery(self):
            return self.getTypedRuleContext(SQLParser.SubqueryContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_table_subquery

        def accept(self, visitor):
            if hasattr(visitor, "visitTable_subquery"):
                return visitor.visitTable_subquery(self)
            else:
                return visitor.visitChildren(self)




    def table_subquery(self):

        localctx = SQLParser.Table_subqueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_table_subquery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1511
            self.subquery()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubqueryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.SubqueryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def query_expression(self):
            return self.getTypedRuleContext(SQLParser.Query_expressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_subquery

        def accept(self, visitor):
            if hasattr(visitor, "visitSubquery"):
                return visitor.visitSubquery(self)
            else:
                return visitor.visitChildren(self)




    def subquery(self):

        localctx = SQLParser.SubqueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 334, self.RULE_subquery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1513
            self.match(SQLParser.LEFT_PAREN)
            self.state = 1514
            self.query_expression()
            self.state = 1515
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PredicateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.PredicateContext, self).__init__(parent, invokingState)
            self.parser = parser

        def comparison_predicate(self):
            return self.getTypedRuleContext(SQLParser.Comparison_predicateContext,0)


        def between_predicate(self):
            return self.getTypedRuleContext(SQLParser.Between_predicateContext,0)


        def in_predicate(self):
            return self.getTypedRuleContext(SQLParser.In_predicateContext,0)


        def pattern_matching_predicate(self):
            return self.getTypedRuleContext(SQLParser.Pattern_matching_predicateContext,0)


        def null_predicate(self):
            return self.getTypedRuleContext(SQLParser.Null_predicateContext,0)


        def exists_predicate(self):
            return self.getTypedRuleContext(SQLParser.Exists_predicateContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_predicate

        def accept(self, visitor):
            if hasattr(visitor, "visitPredicate"):
                return visitor.visitPredicate(self)
            else:
                return visitor.visitChildren(self)




    def predicate(self):

        localctx = SQLParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_predicate)
        try:
            self.state = 1523
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,160,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1517
                self.comparison_predicate()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1518
                self.between_predicate()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1519
                self.in_predicate()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1520
                self.pattern_matching_predicate()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1521
                self.null_predicate()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1522
                self.exists_predicate()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Comparison_predicateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Comparison_predicateContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Row_value_predicandContext
            self.c = None # Comp_opContext
            self.right = None # Row_value_predicandContext

        def row_value_predicand(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Row_value_predicandContext)
            else:
                return self.getTypedRuleContext(SQLParser.Row_value_predicandContext,i)


        def comp_op(self):
            return self.getTypedRuleContext(SQLParser.Comp_opContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_comparison_predicate

        def accept(self, visitor):
            if hasattr(visitor, "visitComparison_predicate"):
                return visitor.visitComparison_predicate(self)
            else:
                return visitor.visitChildren(self)




    def comparison_predicate(self):

        localctx = SQLParser.Comparison_predicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 338, self.RULE_comparison_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1525
            localctx.left = self.row_value_predicand()
            self.state = 1526
            localctx.c = self.comp_op()
            self.state = 1527
            localctx.right = self.row_value_predicand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Comp_opContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Comp_opContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(SQLParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(SQLParser.NOT_EQUAL, 0)

        def LTH(self):
            return self.getToken(SQLParser.LTH, 0)

        def LEQ(self):
            return self.getToken(SQLParser.LEQ, 0)

        def GTH(self):
            return self.getToken(SQLParser.GTH, 0)

        def GEQ(self):
            return self.getToken(SQLParser.GEQ, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_comp_op

        def accept(self, visitor):
            if hasattr(visitor, "visitComp_op"):
                return visitor.visitComp_op(self)
            else:
                return visitor.visitChildren(self)




    def comp_op(self):

        localctx = SQLParser.Comp_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_comp_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1529
            _la = self._input.LA(1)
            if not(((((_la - 174)) & ~0x3f) == 0 and ((1 << (_la - 174)) & ((1 << (SQLParser.EQUAL - 174)) | (1 << (SQLParser.NOT_EQUAL - 174)) | (1 << (SQLParser.LTH - 174)) | (1 << (SQLParser.LEQ - 174)) | (1 << (SQLParser.GTH - 174)) | (1 << (SQLParser.GEQ - 174)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Between_predicateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Between_predicateContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.predicand = None # Row_value_predicandContext

        def between_predicate_part_2(self):
            return self.getTypedRuleContext(SQLParser.Between_predicate_part_2Context,0)


        def row_value_predicand(self):
            return self.getTypedRuleContext(SQLParser.Row_value_predicandContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_between_predicate

        def accept(self, visitor):
            if hasattr(visitor, "visitBetween_predicate"):
                return visitor.visitBetween_predicate(self)
            else:
                return visitor.visitChildren(self)




    def between_predicate(self):

        localctx = SQLParser.Between_predicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_between_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1531
            localctx.predicand = self.row_value_predicand()
            self.state = 1532
            self.between_predicate_part_2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Between_predicate_part_2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Between_predicate_part_2Context, self).__init__(parent, invokingState)
            self.parser = parser
            self.begin = None # Row_value_predicandContext
            self.end = None # Row_value_predicandContext

        def BETWEEN(self):
            return self.getToken(SQLParser.BETWEEN, 0)

        def AND(self):
            return self.getToken(SQLParser.AND, 0)

        def row_value_predicand(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Row_value_predicandContext)
            else:
                return self.getTypedRuleContext(SQLParser.Row_value_predicandContext,i)


        def NOT(self):
            return self.getToken(SQLParser.NOT, 0)

        def ASYMMETRIC(self):
            return self.getToken(SQLParser.ASYMMETRIC, 0)

        def SYMMETRIC(self):
            return self.getToken(SQLParser.SYMMETRIC, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_between_predicate_part_2

        def accept(self, visitor):
            if hasattr(visitor, "visitBetween_predicate_part_2"):
                return visitor.visitBetween_predicate_part_2(self)
            else:
                return visitor.visitChildren(self)




    def between_predicate_part_2(self):

        localctx = SQLParser.Between_predicate_part_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_between_predicate_part_2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1535
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.NOT:
                self.state = 1534
                self.match(SQLParser.NOT)


            self.state = 1537
            self.match(SQLParser.BETWEEN)
            self.state = 1539
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.ASYMMETRIC or _la==SQLParser.SYMMETRIC:
                self.state = 1538
                _la = self._input.LA(1)
                if not(_la==SQLParser.ASYMMETRIC or _la==SQLParser.SYMMETRIC):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 1541
            localctx.begin = self.row_value_predicand()
            self.state = 1542
            self.match(SQLParser.AND)
            self.state = 1543
            localctx.end = self.row_value_predicand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class In_predicateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.In_predicateContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.predicand = None # Numeric_value_expressionContext

        def IN(self):
            return self.getToken(SQLParser.IN, 0)

        def in_predicate_value(self):
            return self.getTypedRuleContext(SQLParser.In_predicate_valueContext,0)


        def numeric_value_expression(self):
            return self.getTypedRuleContext(SQLParser.Numeric_value_expressionContext,0)


        def NOT(self):
            return self.getToken(SQLParser.NOT, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_in_predicate

        def accept(self, visitor):
            if hasattr(visitor, "visitIn_predicate"):
                return visitor.visitIn_predicate(self)
            else:
                return visitor.visitChildren(self)




    def in_predicate(self):

        localctx = SQLParser.In_predicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 346, self.RULE_in_predicate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1545
            localctx.predicand = self.numeric_value_expression()
            self.state = 1547
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.NOT:
                self.state = 1546
                self.match(SQLParser.NOT)


            self.state = 1549
            self.match(SQLParser.IN)
            self.state = 1550
            self.in_predicate_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class In_predicate_valueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.In_predicate_valueContext, self).__init__(parent, invokingState)
            self.parser = parser

        def table_subquery(self):
            return self.getTypedRuleContext(SQLParser.Table_subqueryContext,0)


        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def in_value_list(self):
            return self.getTypedRuleContext(SQLParser.In_value_listContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_in_predicate_value

        def accept(self, visitor):
            if hasattr(visitor, "visitIn_predicate_value"):
                return visitor.visitIn_predicate_value(self)
            else:
                return visitor.visitChildren(self)




    def in_predicate_value(self):

        localctx = SQLParser.In_predicate_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_in_predicate_value)
        try:
            self.state = 1557
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,164,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1552
                self.table_subquery()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1553
                self.match(SQLParser.LEFT_PAREN)
                self.state = 1554
                self.in_value_list()
                self.state = 1555
                self.match(SQLParser.RIGHT_PAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class In_value_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.In_value_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def row_value_expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Row_value_expressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.Row_value_expressionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_in_value_list

        def accept(self, visitor):
            if hasattr(visitor, "visitIn_value_list"):
                return visitor.visitIn_value_list(self)
            else:
                return visitor.visitChildren(self)




    def in_value_list(self):

        localctx = SQLParser.In_value_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_in_value_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1559
            self.row_value_expression()
            self.state = 1564
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.COMMA:
                self.state = 1560
                self.match(SQLParser.COMMA)
                self.state = 1561
                self.row_value_expression()
                self.state = 1566
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pattern_matching_predicateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Pattern_matching_predicateContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.f = None # Row_value_predicandContext
            self.s = None # Token

        def pattern_matcher(self):
            return self.getTypedRuleContext(SQLParser.Pattern_matcherContext,0)


        def row_value_predicand(self):
            return self.getTypedRuleContext(SQLParser.Row_value_predicandContext,0)


        def Character_String_Literal(self):
            return self.getToken(SQLParser.Character_String_Literal, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_pattern_matching_predicate

        def accept(self, visitor):
            if hasattr(visitor, "visitPattern_matching_predicate"):
                return visitor.visitPattern_matching_predicate(self)
            else:
                return visitor.visitChildren(self)




    def pattern_matching_predicate(self):

        localctx = SQLParser.Pattern_matching_predicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 352, self.RULE_pattern_matching_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1567
            localctx.f = self.row_value_predicand()
            self.state = 1568
            self.pattern_matcher()
            self.state = 1569
            localctx.s = self.match(SQLParser.Character_String_Literal)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pattern_matcherContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Pattern_matcherContext, self).__init__(parent, invokingState)
            self.parser = parser

        def negativable_matcher(self):
            return self.getTypedRuleContext(SQLParser.Negativable_matcherContext,0)


        def NOT(self):
            return self.getToken(SQLParser.NOT, 0)

        def regex_matcher(self):
            return self.getTypedRuleContext(SQLParser.Regex_matcherContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_pattern_matcher

        def accept(self, visitor):
            if hasattr(visitor, "visitPattern_matcher"):
                return visitor.visitPattern_matcher(self)
            else:
                return visitor.visitChildren(self)




    def pattern_matcher(self):

        localctx = SQLParser.Pattern_matcherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_pattern_matcher)
        self._la = 0 # Token type
        try:
            self.state = 1576
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.ILIKE, SQLParser.LIKE, SQLParser.NOT, SQLParser.REGEXP, SQLParser.RLIKE, SQLParser.SIMILAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1572
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.NOT:
                    self.state = 1571
                    self.match(SQLParser.NOT)


                self.state = 1574
                self.negativable_matcher()
                pass
            elif token in [SQLParser.Similar_To, SQLParser.Not_Similar_To, SQLParser.Similar_To_Case_Insensitive, SQLParser.Not_Similar_To_Case_Insensitive]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1575
                self.regex_matcher()
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

    class Negativable_matcherContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Negativable_matcherContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LIKE(self):
            return self.getToken(SQLParser.LIKE, 0)

        def ILIKE(self):
            return self.getToken(SQLParser.ILIKE, 0)

        def SIMILAR(self):
            return self.getToken(SQLParser.SIMILAR, 0)

        def TO(self):
            return self.getToken(SQLParser.TO, 0)

        def REGEXP(self):
            return self.getToken(SQLParser.REGEXP, 0)

        def RLIKE(self):
            return self.getToken(SQLParser.RLIKE, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_negativable_matcher

        def accept(self, visitor):
            if hasattr(visitor, "visitNegativable_matcher"):
                return visitor.visitNegativable_matcher(self)
            else:
                return visitor.visitChildren(self)




    def negativable_matcher(self):

        localctx = SQLParser.Negativable_matcherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_negativable_matcher)
        try:
            self.state = 1584
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.LIKE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1578
                self.match(SQLParser.LIKE)
                pass
            elif token in [SQLParser.ILIKE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1579
                self.match(SQLParser.ILIKE)
                pass
            elif token in [SQLParser.SIMILAR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1580
                self.match(SQLParser.SIMILAR)
                self.state = 1581
                self.match(SQLParser.TO)
                pass
            elif token in [SQLParser.REGEXP]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1582
                self.match(SQLParser.REGEXP)
                pass
            elif token in [SQLParser.RLIKE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1583
                self.match(SQLParser.RLIKE)
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

    class Regex_matcherContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Regex_matcherContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Similar_To(self):
            return self.getToken(SQLParser.Similar_To, 0)

        def Not_Similar_To(self):
            return self.getToken(SQLParser.Not_Similar_To, 0)

        def Similar_To_Case_Insensitive(self):
            return self.getToken(SQLParser.Similar_To_Case_Insensitive, 0)

        def Not_Similar_To_Case_Insensitive(self):
            return self.getToken(SQLParser.Not_Similar_To_Case_Insensitive, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_regex_matcher

        def accept(self, visitor):
            if hasattr(visitor, "visitRegex_matcher"):
                return visitor.visitRegex_matcher(self)
            else:
                return visitor.visitChildren(self)




    def regex_matcher(self):

        localctx = SQLParser.Regex_matcherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 358, self.RULE_regex_matcher)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1586
            _la = self._input.LA(1)
            if not(((((_la - 168)) & ~0x3f) == 0 and ((1 << (_la - 168)) & ((1 << (SQLParser.Similar_To - 168)) | (1 << (SQLParser.Not_Similar_To - 168)) | (1 << (SQLParser.Similar_To_Case_Insensitive - 168)) | (1 << (SQLParser.Not_Similar_To_Case_Insensitive - 168)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Null_predicateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Null_predicateContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.predicand = None # Row_value_predicandContext
            self.n = None # Token

        def IS(self):
            return self.getToken(SQLParser.IS, 0)

        def NULL(self):
            return self.getToken(SQLParser.NULL, 0)

        def row_value_predicand(self):
            return self.getTypedRuleContext(SQLParser.Row_value_predicandContext,0)


        def NOT(self):
            return self.getToken(SQLParser.NOT, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_null_predicate

        def accept(self, visitor):
            if hasattr(visitor, "visitNull_predicate"):
                return visitor.visitNull_predicate(self)
            else:
                return visitor.visitChildren(self)




    def null_predicate(self):

        localctx = SQLParser.Null_predicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 360, self.RULE_null_predicate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1588
            localctx.predicand = self.row_value_predicand()
            self.state = 1589
            self.match(SQLParser.IS)
            self.state = 1591
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.NOT:
                self.state = 1590
                localctx.n = self.match(SQLParser.NOT)


            self.state = 1593
            self.match(SQLParser.NULL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Quantified_comparison_predicateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Quantified_comparison_predicateContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.l = None # Numeric_value_expressionContext
            self.c = None # Comp_opContext
            self.q = None # QuantifierContext
            self.s = None # Table_subqueryContext

        def numeric_value_expression(self):
            return self.getTypedRuleContext(SQLParser.Numeric_value_expressionContext,0)


        def comp_op(self):
            return self.getTypedRuleContext(SQLParser.Comp_opContext,0)


        def quantifier(self):
            return self.getTypedRuleContext(SQLParser.QuantifierContext,0)


        def table_subquery(self):
            return self.getTypedRuleContext(SQLParser.Table_subqueryContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_quantified_comparison_predicate

        def accept(self, visitor):
            if hasattr(visitor, "visitQuantified_comparison_predicate"):
                return visitor.visitQuantified_comparison_predicate(self)
            else:
                return visitor.visitChildren(self)




    def quantified_comparison_predicate(self):

        localctx = SQLParser.Quantified_comparison_predicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 362, self.RULE_quantified_comparison_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1595
            localctx.l = self.numeric_value_expression()
            self.state = 1596
            localctx.c = self.comp_op()
            self.state = 1597
            localctx.q = self.quantifier()
            self.state = 1598
            localctx.s = self.table_subquery()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class QuantifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.QuantifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def all(self):
            return self.getTypedRuleContext(SQLParser.AllContext,0)


        def some(self):
            return self.getTypedRuleContext(SQLParser.SomeContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_quantifier

        def accept(self, visitor):
            if hasattr(visitor, "visitQuantifier"):
                return visitor.visitQuantifier(self)
            else:
                return visitor.visitChildren(self)




    def quantifier(self):

        localctx = SQLParser.QuantifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 364, self.RULE_quantifier)
        try:
            self.state = 1602
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.ALL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1600
                self.all()
                pass
            elif token in [SQLParser.ANY, SQLParser.SOME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1601
                self.some()
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

    class AllContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.AllContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ALL(self):
            return self.getToken(SQLParser.ALL, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_all

        def accept(self, visitor):
            if hasattr(visitor, "visitAll"):
                return visitor.visitAll(self)
            else:
                return visitor.visitChildren(self)




    def all(self):

        localctx = SQLParser.AllContext(self, self._ctx, self.state)
        self.enterRule(localctx, 366, self.RULE_all)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1604
            self.match(SQLParser.ALL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SomeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.SomeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SOME(self):
            return self.getToken(SQLParser.SOME, 0)

        def ANY(self):
            return self.getToken(SQLParser.ANY, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_some

        def accept(self, visitor):
            if hasattr(visitor, "visitSome"):
                return visitor.visitSome(self)
            else:
                return visitor.visitChildren(self)




    def some(self):

        localctx = SQLParser.SomeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_some)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1606
            _la = self._input.LA(1)
            if not(_la==SQLParser.ANY or _la==SQLParser.SOME):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Exists_predicateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Exists_predicateContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.s = None # Table_subqueryContext

        def EXISTS(self):
            return self.getToken(SQLParser.EXISTS, 0)

        def table_subquery(self):
            return self.getTypedRuleContext(SQLParser.Table_subqueryContext,0)


        def NOT(self):
            return self.getToken(SQLParser.NOT, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_exists_predicate

        def accept(self, visitor):
            if hasattr(visitor, "visitExists_predicate"):
                return visitor.visitExists_predicate(self)
            else:
                return visitor.visitChildren(self)




    def exists_predicate(self):

        localctx = SQLParser.Exists_predicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 370, self.RULE_exists_predicate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1609
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.NOT:
                self.state = 1608
                self.match(SQLParser.NOT)


            self.state = 1611
            self.match(SQLParser.EXISTS)
            self.state = 1612
            localctx.s = self.table_subquery()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Unique_predicateContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Unique_predicateContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.s = None # Table_subqueryContext

        def UNIQUE(self):
            return self.getToken(SQLParser.UNIQUE, 0)

        def table_subquery(self):
            return self.getTypedRuleContext(SQLParser.Table_subqueryContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_unique_predicate

        def accept(self, visitor):
            if hasattr(visitor, "visitUnique_predicate"):
                return visitor.visitUnique_predicate(self)
            else:
                return visitor.visitChildren(self)




    def unique_predicate(self):

        localctx = SQLParser.Unique_predicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 372, self.RULE_unique_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1614
            self.match(SQLParser.UNIQUE)
            self.state = 1615
            localctx.s = self.table_subquery()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Primary_datetime_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Primary_datetime_fieldContext, self).__init__(parent, invokingState)
            self.parser = parser

        def non_second_primary_datetime_field(self):
            return self.getTypedRuleContext(SQLParser.Non_second_primary_datetime_fieldContext,0)


        def SECOND(self):
            return self.getToken(SQLParser.SECOND, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_primary_datetime_field

        def accept(self, visitor):
            if hasattr(visitor, "visitPrimary_datetime_field"):
                return visitor.visitPrimary_datetime_field(self)
            else:
                return visitor.visitChildren(self)




    def primary_datetime_field(self):

        localctx = SQLParser.Primary_datetime_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 374, self.RULE_primary_datetime_field)
        try:
            self.state = 1619
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.DAY, SQLParser.HOUR, SQLParser.MINUTE, SQLParser.MONTH, SQLParser.YEAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1617
                self.non_second_primary_datetime_field()
                pass
            elif token in [SQLParser.SECOND]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1618
                self.match(SQLParser.SECOND)
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

    class Non_second_primary_datetime_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Non_second_primary_datetime_fieldContext, self).__init__(parent, invokingState)
            self.parser = parser

        def YEAR(self):
            return self.getToken(SQLParser.YEAR, 0)

        def MONTH(self):
            return self.getToken(SQLParser.MONTH, 0)

        def DAY(self):
            return self.getToken(SQLParser.DAY, 0)

        def HOUR(self):
            return self.getToken(SQLParser.HOUR, 0)

        def MINUTE(self):
            return self.getToken(SQLParser.MINUTE, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_non_second_primary_datetime_field

        def accept(self, visitor):
            if hasattr(visitor, "visitNon_second_primary_datetime_field"):
                return visitor.visitNon_second_primary_datetime_field(self)
            else:
                return visitor.visitChildren(self)




    def non_second_primary_datetime_field(self):

        localctx = SQLParser.Non_second_primary_datetime_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 376, self.RULE_non_second_primary_datetime_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1621
            _la = self._input.LA(1)
            if not(((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (SQLParser.DAY - 64)) | (1 << (SQLParser.HOUR - 64)) | (1 << (SQLParser.MINUTE - 64)) | (1 << (SQLParser.MONTH - 64)))) != 0) or _la==SQLParser.YEAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Extended_datetime_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Extended_datetime_fieldContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CENTURY(self):
            return self.getToken(SQLParser.CENTURY, 0)

        def DECADE(self):
            return self.getToken(SQLParser.DECADE, 0)

        def DOW(self):
            return self.getToken(SQLParser.DOW, 0)

        def DOY(self):
            return self.getToken(SQLParser.DOY, 0)

        def EPOCH(self):
            return self.getToken(SQLParser.EPOCH, 0)

        def ISODOW(self):
            return self.getToken(SQLParser.ISODOW, 0)

        def ISOYEAR(self):
            return self.getToken(SQLParser.ISOYEAR, 0)

        def MICROSECONDS(self):
            return self.getToken(SQLParser.MICROSECONDS, 0)

        def MILLENNIUM(self):
            return self.getToken(SQLParser.MILLENNIUM, 0)

        def MILLISECONDS(self):
            return self.getToken(SQLParser.MILLISECONDS, 0)

        def QUARTER(self):
            return self.getToken(SQLParser.QUARTER, 0)

        def WEEK(self):
            return self.getToken(SQLParser.WEEK, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_extended_datetime_field

        def accept(self, visitor):
            if hasattr(visitor, "visitExtended_datetime_field"):
                return visitor.visitExtended_datetime_field(self)
            else:
                return visitor.visitChildren(self)




    def extended_datetime_field(self):

        localctx = SQLParser.Extended_datetime_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 378, self.RULE_extended_datetime_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1623
            _la = self._input.LA(1)
            if not(((((_la - 57)) & ~0x3f) == 0 and ((1 << (_la - 57)) & ((1 << (SQLParser.CENTURY - 57)) | (1 << (SQLParser.DECADE - 57)) | (1 << (SQLParser.DOW - 57)) | (1 << (SQLParser.DOY - 57)) | (1 << (SQLParser.EPOCH - 57)) | (1 << (SQLParser.ISODOW - 57)) | (1 << (SQLParser.ISOYEAR - 57)) | (1 << (SQLParser.MICROSECONDS - 57)) | (1 << (SQLParser.MILLENNIUM - 57)) | (1 << (SQLParser.MILLISECONDS - 57)) | (1 << (SQLParser.QUARTER - 57)))) != 0) or _la==SQLParser.WEEK):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Routine_invocationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Routine_invocationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def function_name(self):
            return self.getTypedRuleContext(SQLParser.Function_nameContext,0)


        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def sql_argument_list(self):
            return self.getTypedRuleContext(SQLParser.Sql_argument_listContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_routine_invocation

        def accept(self, visitor):
            if hasattr(visitor, "visitRoutine_invocation"):
                return visitor.visitRoutine_invocation(self)
            else:
                return visitor.visitChildren(self)




    def routine_invocation(self):

        localctx = SQLParser.Routine_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_routine_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1625
            self.function_name()
            self.state = 1626
            self.match(SQLParser.LEFT_PAREN)
            self.state = 1628
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SQLParser.ANY) | (1 << SQLParser.CASE) | (1 << SQLParser.CAST) | (1 << SQLParser.FALSE) | (1 << SQLParser.LEFT) | (1 << SQLParser.NOT) | (1 << SQLParser.NULL) | (1 << SQLParser.RIGHT) | (1 << SQLParser.SOME) | (1 << SQLParser.TRUE) | (1 << SQLParser.AVG) | (1 << SQLParser.BETWEEN) | (1 << SQLParser.BY) | (1 << SQLParser.CENTURY) | (1 << SQLParser.CHARACTER) | (1 << SQLParser.COLLECT) | (1 << SQLParser.COALESCE) | (1 << SQLParser.COLUMN) | (1 << SQLParser.COUNT) | (1 << SQLParser.CUBE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (SQLParser.DAY - 64)) | (1 << (SQLParser.DEC - 64)) | (1 << (SQLParser.DECADE - 64)) | (1 << (SQLParser.DOW - 64)) | (1 << (SQLParser.DOY - 64)) | (1 << (SQLParser.DROP - 64)) | (1 << (SQLParser.EPOCH - 64)) | (1 << (SQLParser.EVERY - 64)) | (1 << (SQLParser.EXISTS - 64)) | (1 << (SQLParser.EXTERNAL - 64)) | (1 << (SQLParser.EXTRACT - 64)) | (1 << (SQLParser.FILTER - 64)) | (1 << (SQLParser.FIRST - 64)) | (1 << (SQLParser.FORMAT - 64)) | (1 << (SQLParser.FUSION - 64)) | (1 << (SQLParser.GROUPING - 64)) | (1 << (SQLParser.HASH - 64)) | (1 << (SQLParser.INDEX - 64)) | (1 << (SQLParser.INSERT - 64)) | (1 << (SQLParser.INTERSECTION - 64)) | (1 << (SQLParser.ISODOW - 64)) | (1 << (SQLParser.ISOYEAR - 64)) | (1 << (SQLParser.LAST - 64)) | (1 << (SQLParser.LESS - 64)) | (1 << (SQLParser.LIST - 64)) | (1 << (SQLParser.LOCATION - 64)) | (1 << (SQLParser.MAX - 64)) | (1 << (SQLParser.MAXVALUE - 64)) | (1 << (SQLParser.MICROSECONDS - 64)) | (1 << (SQLParser.MILLENNIUM - 64)) | (1 << (SQLParser.MILLISECONDS - 64)) | (1 << (SQLParser.MIN - 64)) | (1 << (SQLParser.MINUTE - 64)) | (1 << (SQLParser.MONTH - 64)) | (1 << (SQLParser.NATIONAL - 64)) | (1 << (SQLParser.NULLIF - 64)) | (1 << (SQLParser.OVERWRITE - 64)) | (1 << (SQLParser.PARTITION - 64)) | (1 << (SQLParser.PARTITIONS - 64)) | (1 << (SQLParser.PRECISION - 64)) | (1 << (SQLParser.PURGE - 64)) | (1 << (SQLParser.QUARTER - 64)) | (1 << (SQLParser.RANGE - 64)) | (1 << (SQLParser.REGEXP - 64)) | (1 << (SQLParser.RLIKE - 64)) | (1 << (SQLParser.ROLLUP - 64)) | (1 << (SQLParser.SECOND - 64)) | (1 << (SQLParser.SET - 64)) | (1 << (SQLParser.SIMILAR - 64)) | (1 << (SQLParser.STDDEV_POP - 64)) | (1 << (SQLParser.STDDEV_SAMP - 64)) | (1 << (SQLParser.SUBPARTITION - 64)) | (1 << (SQLParser.SUM - 64)) | (1 << (SQLParser.TABLESPACE - 64)) | (1 << (SQLParser.THAN - 64)) | (1 << (SQLParser.TIMEZONE - 64)) | (1 << (SQLParser.TIMEZONE_HOUR - 64)) | (1 << (SQLParser.TIMEZONE_MINUTE - 64)) | (1 << (SQLParser.TRIM - 64)) | (1 << (SQLParser.TO - 64)) | (1 << (SQLParser.UNKNOWN - 64)) | (1 << (SQLParser.VALUES - 64)) | (1 << (SQLParser.VAR_SAMP - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (SQLParser.VAR_POP - 128)) | (1 << (SQLParser.VARYING - 128)) | (1 << (SQLParser.WEEK - 128)) | (1 << (SQLParser.YEAR - 128)) | (1 << (SQLParser.ZONE - 128)) | (1 << (SQLParser.BOOLEAN - 128)) | (1 << (SQLParser.BOOL - 128)) | (1 << (SQLParser.BIT - 128)) | (1 << (SQLParser.VARBIT - 128)) | (1 << (SQLParser.INT1 - 128)) | (1 << (SQLParser.INT2 - 128)) | (1 << (SQLParser.INT4 - 128)) | (1 << (SQLParser.INT8 - 128)) | (1 << (SQLParser.TINYINT - 128)) | (1 << (SQLParser.SMALLINT - 128)) | (1 << (SQLParser.INT - 128)) | (1 << (SQLParser.INTEGER - 128)) | (1 << (SQLParser.BIGINT - 128)) | (1 << (SQLParser.FLOAT4 - 128)) | (1 << (SQLParser.FLOAT8 - 128)) | (1 << (SQLParser.REAL - 128)) | (1 << (SQLParser.FLOAT - 128)) | (1 << (SQLParser.DOUBLE - 128)) | (1 << (SQLParser.NUMERIC - 128)) | (1 << (SQLParser.DECIMAL - 128)) | (1 << (SQLParser.CHAR - 128)) | (1 << (SQLParser.VARCHAR - 128)) | (1 << (SQLParser.NCHAR - 128)) | (1 << (SQLParser.NVARCHAR - 128)) | (1 << (SQLParser.DATE - 128)) | (1 << (SQLParser.TIME - 128)) | (1 << (SQLParser.TIMETZ - 128)) | (1 << (SQLParser.TIMESTAMP - 128)) | (1 << (SQLParser.TIMESTAMPTZ - 128)) | (1 << (SQLParser.TEXT - 128)) | (1 << (SQLParser.VARBINARY - 128)) | (1 << (SQLParser.BLOB - 128)) | (1 << (SQLParser.BYTEA - 128)) | (1 << (SQLParser.INET4 - 128)) | (1 << (SQLParser.LEFT_PAREN - 128)) | (1 << (SQLParser.PLUS - 128)) | (1 << (SQLParser.MINUS - 128)))) != 0) or ((((_la - 196)) & ~0x3f) == 0 and ((1 << (_la - 196)) & ((1 << (SQLParser.NUMBER - 196)) | (1 << (SQLParser.REAL_NUMBER - 196)) | (1 << (SQLParser.Identifier - 196)) | (1 << (SQLParser.Character_String_Literal - 196)))) != 0):
                self.state = 1627
                self.sql_argument_list()


            self.state = 1630
            self.match(SQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_names_for_reserved_wordsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Function_names_for_reserved_wordsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LEFT(self):
            return self.getToken(SQLParser.LEFT, 0)

        def RIGHT(self):
            return self.getToken(SQLParser.RIGHT, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_function_names_for_reserved_words

        def accept(self, visitor):
            if hasattr(visitor, "visitFunction_names_for_reserved_words"):
                return visitor.visitFunction_names_for_reserved_words(self)
            else:
                return visitor.visitChildren(self)




    def function_names_for_reserved_words(self):

        localctx = SQLParser.Function_names_for_reserved_wordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 382, self.RULE_function_names_for_reserved_words)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1632
            _la = self._input.LA(1)
            if not(_la==SQLParser.LEFT or _la==SQLParser.RIGHT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_nameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Function_nameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def function_names_for_reserved_words(self):
            return self.getTypedRuleContext(SQLParser.Function_names_for_reserved_wordsContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_function_name

        def accept(self, visitor):
            if hasattr(visitor, "visitFunction_name"):
                return visitor.visitFunction_name(self)
            else:
                return visitor.visitChildren(self)




    def function_name(self):

        localctx = SQLParser.Function_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 384, self.RULE_function_name)
        try:
            self.state = 1636
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLParser.AVG, SQLParser.BETWEEN, SQLParser.BY, SQLParser.CENTURY, SQLParser.CHARACTER, SQLParser.COLLECT, SQLParser.COALESCE, SQLParser.COLUMN, SQLParser.COUNT, SQLParser.CUBE, SQLParser.DAY, SQLParser.DEC, SQLParser.DECADE, SQLParser.DOW, SQLParser.DOY, SQLParser.DROP, SQLParser.EPOCH, SQLParser.EVERY, SQLParser.EXISTS, SQLParser.EXTERNAL, SQLParser.EXTRACT, SQLParser.FILTER, SQLParser.FIRST, SQLParser.FORMAT, SQLParser.FUSION, SQLParser.GROUPING, SQLParser.HASH, SQLParser.INDEX, SQLParser.INSERT, SQLParser.INTERSECTION, SQLParser.ISODOW, SQLParser.ISOYEAR, SQLParser.LAST, SQLParser.LESS, SQLParser.LIST, SQLParser.LOCATION, SQLParser.MAX, SQLParser.MAXVALUE, SQLParser.MICROSECONDS, SQLParser.MILLENNIUM, SQLParser.MILLISECONDS, SQLParser.MIN, SQLParser.MINUTE, SQLParser.MONTH, SQLParser.NATIONAL, SQLParser.NULLIF, SQLParser.OVERWRITE, SQLParser.PARTITION, SQLParser.PARTITIONS, SQLParser.PRECISION, SQLParser.PURGE, SQLParser.QUARTER, SQLParser.RANGE, SQLParser.REGEXP, SQLParser.RLIKE, SQLParser.ROLLUP, SQLParser.SECOND, SQLParser.SET, SQLParser.SIMILAR, SQLParser.STDDEV_POP, SQLParser.STDDEV_SAMP, SQLParser.SUBPARTITION, SQLParser.SUM, SQLParser.TABLESPACE, SQLParser.THAN, SQLParser.TIMEZONE, SQLParser.TIMEZONE_HOUR, SQLParser.TIMEZONE_MINUTE, SQLParser.TRIM, SQLParser.TO, SQLParser.UNKNOWN, SQLParser.VALUES, SQLParser.VAR_SAMP, SQLParser.VAR_POP, SQLParser.VARYING, SQLParser.WEEK, SQLParser.YEAR, SQLParser.ZONE, SQLParser.BOOLEAN, SQLParser.BOOL, SQLParser.BIT, SQLParser.VARBIT, SQLParser.INT1, SQLParser.INT2, SQLParser.INT4, SQLParser.INT8, SQLParser.TINYINT, SQLParser.SMALLINT, SQLParser.INT, SQLParser.INTEGER, SQLParser.BIGINT, SQLParser.FLOAT4, SQLParser.FLOAT8, SQLParser.REAL, SQLParser.FLOAT, SQLParser.DOUBLE, SQLParser.NUMERIC, SQLParser.DECIMAL, SQLParser.CHAR, SQLParser.VARCHAR, SQLParser.NCHAR, SQLParser.NVARCHAR, SQLParser.DATE, SQLParser.TIME, SQLParser.TIMETZ, SQLParser.TIMESTAMP, SQLParser.TIMESTAMPTZ, SQLParser.TEXT, SQLParser.VARBINARY, SQLParser.BLOB, SQLParser.BYTEA, SQLParser.INET4, SQLParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1634
                self.identifier()
                pass
            elif token in [SQLParser.LEFT, SQLParser.RIGHT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1635
                self.function_names_for_reserved_words()
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

    class Sql_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Sql_argument_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def value_expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Value_expressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.Value_expressionContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_sql_argument_list

        def accept(self, visitor):
            if hasattr(visitor, "visitSql_argument_list"):
                return visitor.visitSql_argument_list(self)
            else:
                return visitor.visitChildren(self)




    def sql_argument_list(self):

        localctx = SQLParser.Sql_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 386, self.RULE_sql_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1638
            self.value_expression()
            self.state = 1643
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.COMMA:
                self.state = 1639
                self.match(SQLParser.COMMA)
                self.state = 1640
                self.value_expression()
                self.state = 1645
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Orderby_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Orderby_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ORDER(self):
            return self.getToken(SQLParser.ORDER, 0)

        def BY(self):
            return self.getToken(SQLParser.BY, 0)

        def sort_specifier_list(self):
            return self.getTypedRuleContext(SQLParser.Sort_specifier_listContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_orderby_clause

        def accept(self, visitor):
            if hasattr(visitor, "visitOrderby_clause"):
                return visitor.visitOrderby_clause(self)
            else:
                return visitor.visitChildren(self)




    def orderby_clause(self):

        localctx = SQLParser.Orderby_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 388, self.RULE_orderby_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1646
            self.match(SQLParser.ORDER)
            self.state = 1647
            self.match(SQLParser.BY)
            self.state = 1648
            self.sort_specifier_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sort_specifier_listContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Sort_specifier_listContext, self).__init__(parent, invokingState)
            self.parser = parser

        def sort_specifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Sort_specifierContext)
            else:
                return self.getTypedRuleContext(SQLParser.Sort_specifierContext,i)


        def COMMA(self, i=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_sort_specifier_list

        def accept(self, visitor):
            if hasattr(visitor, "visitSort_specifier_list"):
                return visitor.visitSort_specifier_list(self)
            else:
                return visitor.visitChildren(self)




    def sort_specifier_list(self):

        localctx = SQLParser.Sort_specifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 390, self.RULE_sort_specifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1650
            self.sort_specifier()
            self.state = 1655
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLParser.COMMA:
                self.state = 1651
                self.match(SQLParser.COMMA)
                self.state = 1652
                self.sort_specifier()
                self.state = 1657
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sort_specifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Sort_specifierContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.key = None # Row_value_predicandContext
            self.order = None # Order_specificationContext
            self.null_order = None # Null_orderingContext

        def row_value_predicand(self):
            return self.getTypedRuleContext(SQLParser.Row_value_predicandContext,0)


        def order_specification(self):
            return self.getTypedRuleContext(SQLParser.Order_specificationContext,0)


        def null_ordering(self):
            return self.getTypedRuleContext(SQLParser.Null_orderingContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_sort_specifier

        def accept(self, visitor):
            if hasattr(visitor, "visitSort_specifier"):
                return visitor.visitSort_specifier(self)
            else:
                return visitor.visitChildren(self)




    def sort_specifier(self):

        localctx = SQLParser.Sort_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 392, self.RULE_sort_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1658
            localctx.key = self.row_value_predicand()
            self.state = 1660
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.ASC or _la==SQLParser.DESC:
                self.state = 1659
                localctx.order = self.order_specification()


            self.state = 1663
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLParser.NULL:
                self.state = 1662
                localctx.null_order = self.null_ordering()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Order_specificationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Order_specificationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ASC(self):
            return self.getToken(SQLParser.ASC, 0)

        def DESC(self):
            return self.getToken(SQLParser.DESC, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_order_specification

        def accept(self, visitor):
            if hasattr(visitor, "visitOrder_specification"):
                return visitor.visitOrder_specification(self)
            else:
                return visitor.visitChildren(self)




    def order_specification(self):

        localctx = SQLParser.Order_specificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 394, self.RULE_order_specification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1665
            _la = self._input.LA(1)
            if not(_la==SQLParser.ASC or _la==SQLParser.DESC):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Limit_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Limit_clauseContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.e = None # Numeric_value_expressionContext

        def LIMIT(self):
            return self.getToken(SQLParser.LIMIT, 0)

        def numeric_value_expression(self):
            return self.getTypedRuleContext(SQLParser.Numeric_value_expressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_limit_clause

        def accept(self, visitor):
            if hasattr(visitor, "visitLimit_clause"):
                return visitor.visitLimit_clause(self)
            else:
                return visitor.visitChildren(self)




    def limit_clause(self):

        localctx = SQLParser.Limit_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 396, self.RULE_limit_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1667
            self.match(SQLParser.LIMIT)
            self.state = 1668
            localctx.e = self.numeric_value_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Null_orderingContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Null_orderingContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NULL(self):
            return self.getToken(SQLParser.NULL, 0)

        def FIRST(self):
            return self.getToken(SQLParser.FIRST, 0)

        def LAST(self):
            return self.getToken(SQLParser.LAST, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_null_ordering

        def accept(self, visitor):
            if hasattr(visitor, "visitNull_ordering"):
                return visitor.visitNull_ordering(self)
            else:
                return visitor.visitChildren(self)




    def null_ordering(self):

        localctx = SQLParser.Null_orderingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 398, self.RULE_null_ordering)
        try:
            self.state = 1674
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,179,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1670
                self.match(SQLParser.NULL)
                self.state = 1671
                self.match(SQLParser.FIRST)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1672
                self.match(SQLParser.NULL)
                self.state = 1673
                self.match(SQLParser.LAST)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Insert_statementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(SQLParser.Insert_statementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.path = None # Token
            self.file_type = None # IdentifierContext

        def INSERT(self):
            return self.getToken(SQLParser.INSERT, 0)

        def INTO(self):
            return self.getToken(SQLParser.INTO, 0)

        def table_name(self):
            return self.getTypedRuleContext(SQLParser.Table_nameContext,0)


        def query_expression(self):
            return self.getTypedRuleContext(SQLParser.Query_expressionContext,0)


        def OVERWRITE(self):
            return self.getToken(SQLParser.OVERWRITE, 0)

        def LEFT_PAREN(self):
            return self.getToken(SQLParser.LEFT_PAREN, 0)

        def column_name_list(self):
            return self.getTypedRuleContext(SQLParser.Column_name_listContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(SQLParser.RIGHT_PAREN, 0)

        def LOCATION(self):
            return self.getToken(SQLParser.LOCATION, 0)

        def Character_String_Literal(self):
            return self.getToken(SQLParser.Character_String_Literal, 0)

        def USING(self):
            return self.getToken(SQLParser.USING, 0)

        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def param_clause(self):
            return self.getTypedRuleContext(SQLParser.Param_clauseContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_insert_statement

        def accept(self, visitor):
            if hasattr(visitor, "visitInsert_statement"):
                return visitor.visitInsert_statement(self)
            else:
                return visitor.visitChildren(self)




    def insert_statement(self):

        localctx = SQLParser.Insert_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 400, self.RULE_insert_statement)
        self._la = 0 # Token type
        try:
            self.state = 1705
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,185,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1676
                self.match(SQLParser.INSERT)
                self.state = 1678
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.OVERWRITE:
                    self.state = 1677
                    self.match(SQLParser.OVERWRITE)


                self.state = 1680
                self.match(SQLParser.INTO)
                self.state = 1681
                self.table_name()
                self.state = 1686
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,181,self._ctx)
                if la_ == 1:
                    self.state = 1682
                    self.match(SQLParser.LEFT_PAREN)
                    self.state = 1683
                    self.column_name_list()
                    self.state = 1684
                    self.match(SQLParser.RIGHT_PAREN)


                self.state = 1688
                self.query_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1690
                self.match(SQLParser.INSERT)
                self.state = 1692
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.OVERWRITE:
                    self.state = 1691
                    self.match(SQLParser.OVERWRITE)


                self.state = 1694
                self.match(SQLParser.INTO)
                self.state = 1695
                self.match(SQLParser.LOCATION)
                self.state = 1696
                localctx.path = self.match(SQLParser.Character_String_Literal)
                self.state = 1702
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLParser.USING:
                    self.state = 1697
                    self.match(SQLParser.USING)
                    self.state = 1698
                    localctx.file_type = self.identifier()
                    self.state = 1700
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==SQLParser.WITH:
                        self.state = 1699
                        self.param_clause()




                self.state = 1704
                self.query_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx