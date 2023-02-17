import asyncio
import logging

from src import Processor


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s::%(message)s')

# runninr infinite loop
asyncio.run(Processor.main())
