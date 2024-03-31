init:
	chmod -R +x ./scripts
	./scripts/init_conda_env.sh

setup-server:
	./scripts/active_conda_env.sh
	./scripts/install_llama-cpp-python.sh
	python server.py

server:
	./scripts/active_conda_env.sh
	python -m llama_cpp.server --model models/phind-codellama-34b-v2.Q4_K_M.gguf

setup:
	./scripts/active_conda_env.sh
	./scripts/install_metal_ctransformers.sh
	pip install -r requirements.txt

start:
	./scripts/active_conda_env.sh
	flask --app main run
