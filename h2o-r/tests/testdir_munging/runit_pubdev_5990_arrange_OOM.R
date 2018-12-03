setwd(normalizePath(dirname(R.utils::commandArgs(asValues=TRUE)$"f")))
source("../../scripts/h2o-r-test-setup.R")

test_arrange_OOM<- function(){
  Log.info('uploading testing dataset')
  df <- h2o.importFile(locate("bigdata/laptop/jira/sort_OOM.csv"))
  df_sorted <- h2o.arrange(df, desc(sort_col))

  res <- as.data.frame(df_sorted$sort_col)
  for (rindex in c(200000:200100)) {
    expect_true(res[rindex, 1] <= res[rindex-1,1], "Sorting error!")
  }
}

doTest('Test h2o.arrange OOM case', test_arrange_OOM)
