CONTAINER_IMAGE = stream-server-local

build: build
	docker build -t $(CONTAINER_IMAGE) .
.PHONY: build
