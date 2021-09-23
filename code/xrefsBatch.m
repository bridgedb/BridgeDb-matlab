function response = xrefsBatch(filepath, org, source)				%Three arguments are needed to execute this function; 1. the path to file containing IDs (each on a new line) 2. the organism name (Latin name, e.g. Homo sapiens) 3. the source database System code, see https://bridgedb.github.io/pages/system-codes.html .
    data = fileread(filepath);							%Reading in the file with IDs to be translated.
    options = weboptions('ContentType','text');
    
    ws_call = 'https://webservice.bridgedb.org/%s/xrefsBatch/%s';		%Defining the xrefBatch URL.
    response = webwrite(sprintf(ws_call, org, source), data, options);		%Executing the webservice call on the arguments defined when calling the function.

    fid = fopen('BridgeDb-matlab/testData/response.txt','w');						%Opening a file to record the response as a .txt file.
    fprintf(fid,'%s',response);							%Writing the response information to the file.
    fclose(fid);								%Closing the file.
    system('python BridgeDb-matlab/code/to_df.py BridgeDb-matlab/testData/response.txt');				%Py: Executing the Python code (to_df.py) on the .txt file.
end
