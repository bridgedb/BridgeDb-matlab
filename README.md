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
- Visit the [matlab online page](https://www.mathworks.com/products/matlab-online.html)
- [Upload the folder](https://nl.mathworks.com/help/matlabmobile/ug/use-files-on-the-cloud.html) where you donwloaded this code (e.g. BridgeDb-matlab) to your [Matlab Drive](https://drive.matlab.com/).

![MatlabOnline_Upload](https://user-images.githubusercontent.com/26277832/133572946-807455f6-e6fb-41b6-9792-13e201dbc587.png)

When the upload succeeded, you should see the BridgeDb-Matlab folde rin your drive, and in you Matlab Online Instance:
![MatlabOnline_drive](https://user-images.githubusercontent.com/26277832/133573305-d8061c35-b170-4cef-bbd1-f44b21cd43ac.png)

![MatlabOnline_workingdirectory](https://user-images.githubusercontent.com/26277832/133573480-2f66646c-cf31-462f-aaf2-fad15e8b0556.png)

- Add the folder to your working directory:

![MatlabOnline_addToPath](https://user-images.githubusercontent.com/26277832/133573880-943b7da1-ab75-450a-95d9-5bd3c309c53c.png)

