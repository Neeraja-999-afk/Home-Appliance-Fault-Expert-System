# Home Appliance Fault Expert System — Updated
This version changes the UI so that selecting an appliance displays only the faults related to that appliance. Selecting a fault then applies the corresponding IF–THEN rule and displays the possible fault and troubleshooting suggestions.

## Run
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:5000`.

## Flow
User Input → Appliance → Related Faults → IF–THEN Rule → Inference → Result/Recommendation

## GitHub
```powershell
git init
git add .
git commit -m "Home Appliance Fault Expert System"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```
