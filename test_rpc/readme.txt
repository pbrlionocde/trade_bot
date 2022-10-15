you must change the MNEMONIC constant in the Dockerfile before running (third argument in CMD)

docker build -t ganache .
docker run -p 8545:8545 ganache
