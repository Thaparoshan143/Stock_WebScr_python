<h1>Python Web Scrapping Program For Stocks of NEPSE </h1>

This is python program aimed to get the Market Price of the given script using beautiful soup for web request and getting the required element for Market Price. It also can be extended to get other infomation with getting the appropriate element/scaning

<h2>Main Program:</h2> <h3>web_scrapper.py</h3>
    -<li>ets the Market Price of given scripts (scripts are in file Scripts_Name.txt) using web request</li>
    <li>compare the current market price with the tolerance price (tolerance are in file Scripts_Tol.txt) (which is randomly generated using Tol_Generator.py for testing... right now)</li>
    <li>if current market price is less than Tolereance, it prints the details at terminal with remarks "Buy" and also writes in the file for further looking if any missed in terminals.</li>

<h3>Note:</h3>
    <li>file name are assigned directly, if required to change change accordingly.</li>
    <li>Currently scripts name contains the scripts that are listed securitiies of NEPSE (Total of 220 companies) till now, you are free to modify the scripts name as per your need (i.e filtering only the required scripts)</li>

<h3>Warning:</h3>
    <li>the scripts name and the tol number should equal to not throw error.
        <li>i.e the count of script in Scripts_Name.txt file and Tol value in Scripts_Tol.txt should be same</li></li>
    <li>only use the Tol_Generator.py if testing is required...</li>
    <li>Modify the value of Scripts_Tol.txt according to the exact order that you have in Scripts_Name.txt (i.e order matters)</li>
    <li>web request are too expensive in terms of performance with entire code being parsed, so not optimized.</li>


Other featurea are also comming soon!
Feel free to download the code and modify the code as per need
