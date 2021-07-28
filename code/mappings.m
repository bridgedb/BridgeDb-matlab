function response = mappings(filepath, org, source)
    data = fileread(filepath);
    options = weboptions('ContentType','text');
    
    ws_call = 'https://webservice.bridgedb.org/%s/xrefsBatch/%s';
    response = webwrite(sprintf(ws_call, org, source), data, options);

    fid = fopen('response.txt','w');
    fprintf(fid,'%s',response);
    fclose(fid);
    system('python to_df.py response.txt');
end