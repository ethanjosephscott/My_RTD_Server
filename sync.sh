#!/bin/bash

cd /var/www/My_RTD_Server/

git --git-dir=/var/www/My_RTD_Server/.git --work-tree=/var/www/My_RTD_Server fetch --quiet

if ! git --git-dir=$/var/www/My_RTD_Server/.git --work-tree=/var/www/My_RTD_Server diff --quiet origin
then
        ## for changes to stick, you need to pull them otherwise it will always have changes
        git --git-dir=/var/www/My_RTD_Server/.git --work-tree=/var/www/My_RTD_Server pull --quiet
        
	source venv/bin/activate

	cd /var/www/My_RTD_Server/docs

	make html
	## do stuff
fi
