#!/bin/bash

docker run --rm=false -t -v $WORKDIR:/work -v $HOME/examples:/data/examples:ro -w /work -e CI_SKIP_TEST=1 -e NIPYPE_RESOURCE_MONITOR=1 -e FSL_COURSE_DATA="/data/examples/nipype-fsl_course_data" "${DOCKER_IMAGE}:py27" /usr/bin/run_pytests.sh
