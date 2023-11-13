.. include:: common.rst


###############################################
SmartRun Machine Learning and GK list reducer
###############################################

This document is really just Bob's notes on issues with exploring 
integrating GK list reducer with the infrastructure used in SmartRun.   They would be in 
OneNote if he was better at working with Microsoft tools.

The source is markdown in the (somewhat poorly named) https://github.com/bobjcondon/rylml.git
Much of the information is covered in various documents owned by the SmartRun team so this content will
eventually migrate to there.

SmartRun
----------

Smartrun uses Machine Learning (ML) to convert a long running testlist
to a much shorter testlist with similar correctness criteria.

It is based on work from the software-testing world taking inspiration from this
work at facebook.

* `Overview <https://engineering.fb.com/2018/11/21/developer-tools/predictive-test-selection>`_
* `Detailed ACM paper <https://arxiv.org/pdf/1810.05286.pdf>`_


There are lots of ML resources available within Intel.   One place to start is
`PESGMachineLearningCOE <https://intel.sharepoint.com/sites/PESGMachineLearningCOE/SitePages/Machine-Learning-Resources.aspx>`_

SmartRun maintains its ML material at 
`SmartRun OneNote <https://intel.sharepoint.com/sites/pesgtegvalidationmanagement/_layouts/OneNote.aspx?id=%2Fsites%2Fpesgtegvalidationmanagement%2FShared%20Documents%2FMachineLearning%2FMachineLearning
onenote:https://intel.sharepoint.com/sites/pesgtegvalidationmanagement/Shared%20Documents/MachineLearning/MachineLearning/>`_

Overall Architecture
---------------------
  TODO -- insert link here

Our Current features
---------------------

The full database of our current features can be queried at the "swagger" database
https://ml.dv.cheetah.sc.intel.com/db/api/v3.4/index.html

Basically we have the "join" of the CthFlow, Dut, GitBase, GitCommit, GitFile, Projects, and Rpt Tables


* Information gleaned from Git
  
  * git_bases_id
  * git_remote_url
  * git_commits_id
  * rev
  * commit_msg

* How "big" the change was.   We currently use the aggregate across all file changes.
  but we have the data available to us on a file by file basis.   This is a very
  crude estimate of the amount of change.   See future work for why and what we 
  plan to do about it.
  
  * commit_total_deleted_lines
  * commit_total_added_lines
  * total_edited_lines

* When and who committed the changes in this submission
  
  * commit_date
  * commit_author
  * commit_author_date    # I think this ends up being the same as commit date

* model
* dut
* seed
* Test length

  * date_time_run
  * date_time_end
  * date_time_sec   # (date_time_end - date_time_run) as seconds

* These two fields seem to be duplicates
  
  * test_status
  * test_result   # as reported in the RPT file

* The test command line is taken as a long string.   See future work for why this is
  inadequate.
  
  * test_cmd_line


Our original features
---------------------

Originally we included the above but with much more detailed information about the 
per-file changes within the design and the testbench.   We stored information
(essentially the output of `diff`) for each file changed.   We could use that information
in conjunction with a verilog parser to produce a much more useful metric of the 
size of the change.    The data involved proved to be excessive for the current 
Splunk implementation to handle.   Removing this measure of the size of the change
caused the accuracy of our model to deteriorate.


Going forward
--------------

Of high importance is restoring the "more accuracy of the diff".   We have acccess 
to two different Verilog parsers (a python-based "approximate" parser) and the Defacto
complete verilog parser.   We will use one of these (presumably the DeFacto parser)
to build "before" and "after" models of the design and extract out features such as

* the overall complexity of the design
* how many {modules, ports, nets ... } were changed.
* were the changes in testbench code or actual design


We currently preserve the entire trex command line.   We believe we should parse 
it to extract more detailed features (perhaps the union of all the verilog defines).


Running Smartrun
------------------



Questions
-----------

* Bernd -- What is the current accuracy of smartrun?   We have presented data showing
  accuracy in the 95+ % range.   Is that using the details of verilog which we 
  no longer get due to splunk limitations.

* Bob to follow up with {Bernd, Thomas, Helge}
  How do we convert file data (list of files changed) to some form of useful 
  categorical data?   

