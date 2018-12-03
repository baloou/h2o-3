from __future__ import print_function
import sys
sys.path.insert(1,"../../")
import h2o
from tests import pyunit_utils

def test_arrange_OOM():
    '''
    PUBDEV-5990 customer reported that h2o.arrange (sorting) takes way more memory than normal for sparse
    datasets of 1G.

    Thanks to Lauren DiPerna for finding the dataset to repo the problem.
    '''

    df = h2o.import_file(pyunit_utils.locate("bigdata/laptop/jira/sort_OOM.csv"))
    newFrame = df.sort("sort_col")
    sortCol = newFrame["sort_col"].as_data_frame(use_pandas=False)
    nrow = df.nrow+1

    # check and make sure the sort columns contain the right value after sorting!
    for ind in range(2,nrow):
        assert float(sortCol[ind-1][0]) <= float(sortCol[ind][0]), "Sorting failed for row {0}.  Value at previous row is {1} and value " \
                                               "at current row is {2}".format(ind-1, sortCol[ind-1], sortCol[ind])


if __name__ == "__main__":
    pyunit_utils.standalone_test(test_arrange_OOM)
else:
    test_arrange_OOM()
