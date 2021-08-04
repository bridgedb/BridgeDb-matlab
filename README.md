# BridgeDbMatlab functions

Functions to use the BridgeDb webservice in Matlab. BridgeDb is a tool for identifier mapping.

Learn about BridgeDb at http://www.bridgedb.org/ and read about it in this paper:

Van Iersel, M.;  Pico, A.;  Kelder, T.;  Gao, J.;  Ho, I.;   Hanspers, K.;  Conklin, B.;  Evelo, C. BMC Bioinformatics 2010, 11, 5, https://doi.org/10.1186/1471-2105-11-5

The DOI of this repository is ADD-DOI

License: [AGPL-3](../main/LICENSE.txt)


# BridgeDb-matlab Usage Instructions:

Please download Matlab first, as well as Python ([instructions](https://nl.mathworks.com/help/matlab/matlab_external/install-supported-python-implementation.html)).
For Python, check if you use a supported version on the command line (Bash/Unix users):
```
python -V
```
Check if Python is setup correctly in Matlab, from the Matlab Command Window:

```Matlab
pe = pyenv
```
Download this repository:
```
git clone https://github.com/bridgedb/BridgeDb-matlab.git
```
Local Matlab installation:
- Start your version of Matlab [tested with Matlab 2021A]
- Add the folder where you donwloaded this code (e.g. BridgeDb-matlab) to your working directory:
Right-click, 'Add to Path'/'Selected Folders and Subfolders'

![image](https://user-images.githubusercontent.com/26277832/128179863-0ec98cfc-a93b-4600-a24e-44e08fed04f3.png)

- Open the folder (double click or rightclick/Open).
Your Current folder in Matlab should look like this now:

![image](https://user-images.githubusercontent.com/26277832/128179968-e1d504e5-8622-461f-af70-ad23b205a0a4.png)

- In the Matlab command window, type the following command to check your pathway directory:
```Matlab
pwd
```
- Execute the XrefsBatch mapping function on the test data, located in the 'testData' folder, as such:
```Matlab
 xrefsBatch('testData/case1-example.tsv', 'Homo sapiens', 'H')
 ```
- Your results are stored in your working directory, as a file called 'mappings.csv' :

![image](https://user-images.githubusercontent.com/26277832/128185709-f21fd6d6-5ee8-422b-b224-6e2398e0aa41.png)

- You can view your results by double clicking the mappings.csv file in the Matlab working directory:

![image](https://user-images.githubusercontent.com/26277832/128186171-d2e5beb9-48a7-4b87-9616-7d90b618afd7.png)


Matlab Online:
...tba...
