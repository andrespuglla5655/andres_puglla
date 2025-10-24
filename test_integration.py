import subprocess

def test_app_output():
    result = subprocess.run(["python", "app.py"], capture_output=True, text=True)
    assert "La suma es: 8" in result.stdout
