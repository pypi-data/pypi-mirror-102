
from ._common import *

# ***************************************************************************************

# namespace
class _rules:

    word = lexer2.Rule("WORD",        r"[a-zA-Z]+")
    # word = lexer2.Rule("WORD",        r"[^。]+")
    punc = lexer2.Rule("PUNCTUATION", r"[.,!]")

    # comment = lexer2.predefs.Comment([
    #     lexer2.predefs.SinglelineComment(r"\/\/"),
    #     lexer2.predefs.MultilineComment(r"\/\*", r"\*\/"),
    # ])


    sl_comment = lexer2.predefs.SinglelineComment(r"\/\/")
    ml_comment = lexer2.predefs.MultilineComment(r"\/\*", r"\*\/")

    RULESET = [
        punc,
        word,
        sl_comment,
        ml_comment
    ]


class Test_MultispanComment (unittest.TestCase):

  # --- ATTRIBUTES SETUP --- #

    def setUp(self) -> None:

        self.options = lexer2.lexer.LexerOptions()
        # self.options.newline.returnTokens = True
        # self.options.returnRule[lexer2.predefs.comment] = True

        # _rules.sl_comment.returnTokens = True
        # _rules.ml_comment.returnTokens = True

        return


  # --- UNIT TESTS --- #

    def test_MultispanComment_01(self):

        self.setUp()

        # Setup
        lexer = lexer2.MakeLexer(
            ruleset=_rules.RULESET,
            options=self.options,
            # textstream=lexer2.file.MakeTextstream(
            #     chunkSize=10,
            #     isBuffered=True
            # )
        )
        lexer.Open(
            # DIR_OF(__file__) / "data/multispan_comment_01.txt",
            DIR_OF(__file__) / "data/multibyte_characters_01.txt",
            bufferSize=0,
            # encoding="UTF-8",
            # encoding="shift_jis",
            convertLineEndings=True
        )

        # Token matching tests
        token: lexer2.Token

        word_tokens = []
        punctuation_tokens = []
        comment_tokens = []

        while(1):

            try: token = lexer.GetNextToken()
            except lexer2.excs.EndOfData:
                break

            if (token.IsRule(_rules.word)):
                word_tokens.append(token)

            elif (token.IsRule(_rules.punc)):
                punctuation_tokens.append(token)

            elif (token.IsRule(lexer2.predefs.comment)):
                comment_tokens.append(token)

            info = [
                "ln: {}".format(token.position.ln +1),
                "col: {}".format(token.position.col+1),
                token.id,
                token.data,
            ]
            print("{: <12} {: <20} {: <20} {: <20}".format(*info))

            # if (token.data == "libero"):
            #     print("")

        # self.assertEqual( len(word_tokens)        , 33 )
        # self.assertEqual( len(punctuation_tokens) ,  6 )
        # self.assertEqual( len(comment_tokens)     ,  2 )

        # self.assertEqual( word_tokens[-1].position.ln  , 50-1 )
        # self.assertEqual( word_tokens[-1].position.col , 14-1 )

        # self.assertEqual( len(comment_tokens[0].data) ,  2126 )
        # self.assertEqual( len(comment_tokens[1].data) ,  1218 )
