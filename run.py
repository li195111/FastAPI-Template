import threading
import uvicorn

from main import app

original_callback = uvicorn.main.callback

def callback(**kwargs):
    from celery.contrib.testing.worker import start_worker

    import tasks

    with start_worker(tasks.task, perform_ping_check=False, loglevel="info"):
        original_callback(**kwargs)

uvicorn.main.callback = callback

if __name__ == "__main__":
    import os
    import sys
    # Execute redis-server
    t = threading.Thread(target=os.system,args=('redis-server',)) 
    t.start()
    # uvicorn filename:app 
    sys.argv += ['main:app','--reload','--host=0.0.0.0','--port=3000']
    uvicorn.main()
    t.join()
