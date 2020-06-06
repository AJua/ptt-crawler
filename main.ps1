while($true){
    python .\get-data.py;
    python .\index.py;
    rm *.json; 
}
