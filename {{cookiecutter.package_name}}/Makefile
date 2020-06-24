package_name = {{ cookiecutter.package_name }}

docker_opts = \
	--rm
docker_compose_opts = -f docker-compose.yml
pytest_opts = \
	-vvv \
	--cov=$(package_name) \
	--cov-branch \
	--cov-report=term \
	--cov-report=html

image = $(package_name)
image_base = $(image)_base
image_dev = $(image)_dev

export APP_IMAGE = $(image)
export APP_IMAGE_DEV = $(image_dev)
define docker_run_dev
	docker-compose $(docker_compose_opts) run $(docker_opts) dev $(1)
endef


build:
	docker build --target base -t $(image_base) .
ifeq ("$(wildcard Pipfile.lock)","")
	$(MAKE) lock
endif
	docker build --target dev -t $(image_dev) .
	docker build -t $(image) .

lock: docker_opts += --volume $(PWD):/workspace
lock:
	docker run $(docker_opts) $(image_base) pipenv lock

shell:
	$(call docker_run_dev,bash)

up:
	docker-compose $(docker_compose_opts) up

down ps:
	docker-compose $@

lint:
	$(call docker_run_dev,pylint $(package_name) tests)

test:
	$(call docker_run_dev,pytest $(pytest_opts) tests)

bump-version:
ifeq ($(BUMP),)
	$(error BUMP=major|minor|patch make bump-version)
endif
	$(call docker_run_dev,bumpversion $(BUMP))