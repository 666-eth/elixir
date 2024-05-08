# elixir
sed -i 's|^ENV ADDRESS=.*|ENV ADDRESS=0x0|; s|^ENV PRIVATE_KEY=.*|ENV PRIVATE_KEY=0x1|' ~/Dockerfile

docker build . -f Dockerfile -t elixir-validator

docker run -d --restart unless-stopped --name ev elixir-validator




docker kill ev
docker rm ev
docker pull elixirprotocol/validator:testnet-2
docker build . -f Dockerfile -t elixir-validator


docker run -d --restart unless-stopped --name ev elixir-validator

