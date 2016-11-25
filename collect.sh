if [ -f /Users/emiliobarreiro/UCR/CareerCenterApp/output.txt ]; then
	rm output.txt
fi
# making sure a clean text file is present for new raffle winner's name and info

touch output.txt
python raffle.py > output.txt
