import unittest
from unittest.mock import patch
from hiscores.rs_hiscores_lookup import HiscoresScraper


class TestRsHiscoresLookup(unittest.TestCase):

    KrabbyResponse = """315667,1590,48349231
                        330516,81,2295731
                        309392,81,2196511
                        315146,91,6061106
                        303654,91,6426255
                        236071,93,7260244
                        21176,99,13046634
                        402800,83,2903257
                        362539,73,1087917
                        1128799,55,170689
                        942559,44,61223
                        396941,71,814592
                        910518,50,103415
                        524698,61,322275
                        470763,60,274608
                        683567,60,273789
                        176937,72,957822
                        538132,60,296956
                        332784,59,266725
                        309730,77,1498183
                        192602,74,1176523
                        402667,44,60480
                        594691,41,42477
                        194435,70,751819
                        -1,-1
                        -1,-1
                        -1,-1
                        771202,2
                        -1,-1
                        -1,-1
                        -1,-1
                        -1,-1
                        178802,2
                        -1,-1"""

    KrabbyResponse2 = """315667,1590,48349231
                        330516,81,2295731
                        309392,81,2196511
                        315146,91,6061106
                        303654,91,6426255
                        236071,93,7260244
                        21176,99,13046634
                        402800,83,2903257
                        362539,73,1087917
                        1128800,55,170689
                        942559,44,61223
                        396941,71,814592
                        910518,50,103415
                        524698,61,322275
                        470763,60,274608
                        683567,60,273789
                        176937,72,957822
                        538132,60,296956
                        332784,59,266725
                        309730,77,1498183
                        192602,74,1176523
                        402667,44,60480
                        594691,41,42477
                        194435,70,751819
                        -1,-1
                        -1,-1
                        -1,-1
                        771202,2
                        -1,-1
                        -1,-1
                        -1,-1
                        -1,-1
                        178802,2
                        -1,-1"""

    @patch('hiscores.rs_hiscores_lookup.HiscoresScraper.fetch_hiscores')
    def test_get_hiscores(self, mocked):
        mocked.return_value = self.KrabbyResponse
        Krabby = HiscoresScraper('krabby', 'normal', 'osrs')
        self.assertEqual(Krabby.json_get_skill('Woodcutting'), '{"rank": 1128799, "level": 55, "exp": 170689}')
        mocked.return_value = self.KrabbyResponse2
        Krabby.refresh_hiscores()
        self.assertEqual(Krabby.json_get_skill('Woodcutting'), '{"rank": 1128800, "level": 55, "exp": 170689}')
