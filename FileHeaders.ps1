git clone https://github.com/an-prata/FileHeaders --quiet
Set-Location FileHeaders

python FileHeaders.py $args
Set-Location ..

Remove-Item -Path FileHeaders -Force -Recurse