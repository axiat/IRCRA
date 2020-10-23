#!/bin/bash
echo "this script is to rename picture"

for names in $(cat list)
        do
                echo "$names"
                    news=$i
                        echo "$news"
                            mv $names "xqn_$news.jpg"
                                let i=i+1
                        done
