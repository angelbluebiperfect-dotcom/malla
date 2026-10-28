from todor import create_app
from todor import elabora
import os
c=0

if __name__ == '__main__':
    
    app= create_app()
    
    app.run(host="0.0.0.0",port=300,debug=True)