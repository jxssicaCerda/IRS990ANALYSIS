# IRS990ANALYSIS

In class project devloping a Python script to extract elements of interest on specific nonprofit forms from over two million field 990 forms from the IRS website. Using regular expressions my function solely focused on nonprofits where the term, 'education' was found within their mission description. My function extracted various elements including Total Employee count, asset count, contribution amount, yearly revenue amount, and EIN.

Parallel programming was used to create 10 parallel workers to execute the 'extract' function across all two million field 990 forms. The result was a dictionary that was filtered through to only keep the five educational nonprofits with the largest yearly revenue amount from the year 2020.
'pandas' and 'deepcopy' was used in this progress to convert the dictionary to a csv file that was imported to R where the final tax analysis occurred.
