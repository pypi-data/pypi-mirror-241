# Regression test on International_Klimaatstrategie

This document is in 'magazine-style', meaning that a single pdf-page
actually consists of 2 normal pages. Each of these pages is even
subdivided into multiple columns. If we want to have even the slightest
hope of processing this document correctly, we need a specific
LaParams()-set in pdfminer for this situation so that it will adhere
to the column-style. This is something the code currently does wrong
for multi-column pages. 2-columns goes (almost) correct and 1-column
is completely correct, but more complicated structures such as
tables and magazine-styles are just not covered yet. So it is
pointless to make a regression test for such a document as long as
there is no real customer-value for these types of documents.
