import solution as s
from synchronous_solution import get_earthquakes_sync
from solution import get_earthquakes_async
from datetime import datetime

ans = ['usc000mqef', 'usc000mchp', 'usc000mc94', 'usb000m8w7', 'usb000m8hj', 'usb000m8af', 'usb000m7ie', 'usb000m6u0', 'usb000m3yf', 'usb000m2jx', 'usb000m22d', 'usb000m20t', 'usb000m20a', 'usb000m0ui', 'usc000m1ki', 'usc000m12p', 'usc000m0yj', 'usc000m0x5', 'usc000m0t5', 'usc000lzju', 'usc000lzdf', 'usc000lzbq', 'usc000lz8y', 'usc000lz8n', 'usc000lz7t', 'usc000lyp5', 'usc000lyi5', 'usc000ly6j', 'usc000ly2l', 'usc000lxrm', 'usc000lwbt', 'usc000lvt0', 'usc000lvk3', 'usb000my9c', 'usb000mxzr', 'usc000mxp3', 'usc000mxnk', 'usc000mx2c', 'usc000mvp7', 'usc000muef', 'usc000msrk', 'usc000msnl', 'usc000mrzt', 'usc000mr39', 'usc000mpy0', 'usc000mmxr', 'usc000mm5y', 'usc000mm4j', 'usc000mm2e', 'usc000mlx1', 'usc000mlm2', 'usc000mktr', 'usc000mkag', 'usc000mj4m', 'usc000mj1u', 'usc000mi5d', 'usc000mgux', 'usc000mgqe', 'usc000mgpp', 'usc000mfkl', 'usc000mfee', 'usc000mf36', 'usb000n0jz', 'usb000n1dt', 'usb000mzdx', 'usc000mcu0', 'usb000m9lh', 'usb000m8mw', 'usb000m8mu', 'usb000m8fx', 'usb000m6iq', 'usb000m5zp', 'usb000m4bh', 'usb000m4be', 'usb000m1z7', 'usb000m0se', 'usc000lyaj', 'usc000lxsm', 'usc000lxr3', 'usc000lxg7', 'usc000lx68', 'usc000lx58', 'usc000lx54', 'usc000lw6l', 'usc000lv5e', 'usb000myj9', 'usb000my0i', 'usc000mxt4', 'usc000mxmd', 'usc000mx1n', 'usc000mwip', 'usc000mte4', 'usc000mst6', 'usc000mrq6', 'usc000mrie', 'usc000mkv5', 'usc000mjh5', 'usc000mtif', 'usc000mgr2', 'usc000mfqw', 'usc000mflt', 'usc000mfjt', 'usc000men8', 'usc000pe7p', 'usb000n00l', 'usb000mztz', 'usb000mzqq', 'usb000mzih', 'usb000m8ca', 'usb000m8bv', 'usb000m89n', 'usc000mkb3', 'usb000m5l1', 'usb000m4u9', 'usb000m3ce', 'usb000m2h5', 'usb000m2ca', 'usb000m1d3', 'usb000m0r8', 'usc000ly2f', 'usc000lwgg', 'usc000lvhr', 'usb000myuk', 'usb000mxzt', 'usc000mu5l', 'usc000mq0k', 'usc000mp11', 'usc000mnln', 'usc000mmrh', 'usc000mmqn', 'usc000mm3n', 'usc000mkir', 'usc000mkcq', 'usc000mh97', 'usc000mgff', 'usc000mftb', 'usc000mfr6', 'usb000mztm', 'usb000mzeu', 'usc000mcfd', 'usb000m8wn', 'usb000m8ad', 'usb000m7by', 'usb000m425', 'usb000m3ke', 'usb000m22z', 'usb000m0ry', 'usc000m0cx', 'usc000lyrv', 'usc000ly19', 'usc000lxaa', 'usc000lwx9', 'usc000lwnk', 'usc000lvtq', 'usc000myx0', 'usc000mxj0', 'usc000mx0u', 'usc000mww2', 'usc000mwin', 'usc000mu59', 'usc000mtb4', 'usc000msg6', 'usc000mmd5', 'usc000mic2', 'usc000mi97', 'usc000mfp8', 'usc000mf7i', 'usb000mzhr', 'usb000mzfd', 'usb000m8gr', 'usb000m81z', 'usb000m3xq', 'usc000lzgt', 'usc000lxfa', 'usc000mxnq', 'usc000mry2', 'usc000mrtv', 'usc000mrqi', 'usc000mm4n', 'usc000mf7v', 'usb000mzjs', 'usb000m6hr', 'usb000m635', 'usb000m225', 'usc000m0xb', 'usc000lx2l', 'usc000lwp7', 'usc000mxmu', 'usc000mxmh', 'usc000mwta', 'usc000mruf', 'usc000mmb5', 'usc000miyu', 'usc000miql', 'usc000mcsn', 'usc000mcj6', 'usb000m8x1', 'usc000mn0r', 'usb000m668', 'usc000lzsc', 'usc000mxn0', 'usc000mxls', 'usc000msj8', 'usc000mqd1', 'usc000mp97', 'usc000mnzc', 'usc000mfvh', 'usb000m6jk', 'usc000lykc', 'usc000lyi1', 'usc000lwmk', 'usc000mz3i', 'usc000ml4s', 'usc000mfe4', 'usb000n0mp', 'usb000m6jc', 'usc000lz8g', 'usc000mslg', 'usc000mgma', 'usb000mzlz', 'usc000mt6q', 'usc000mij1', 'usc000mlk4', 'usc000mfuh', 'usb000mzqn', 'usb000m8ch', 'usb000m7wd', 'usb000m5ge', 'usb000m4i4', 'usc000myqq', 'usc000mf4j', 'usb000mzef', 'usc000m1w9', 'usc000lvb5', 'usc000mskt', 'usc000mjye', 'usc000mfm0', 'usb000mzmn', 'usc000mnvj']

start_date = datetime.strptime("2014-01-01", "%Y-%m-%d")
end_date = datetime.strptime("2014-03-05", "%Y-%m-%d")

def test_baseline(benchmark):
    func = lambda : fibonacci(20)
    result = benchmark(func)
    assert result == 6765

def test_synchronous(benchmark):
    ids = benchmark(get_earthquakes_sync, start_date = start_date, end_date = end_date)
    assert ids == ans

def test_async(benchmark):
    ids = benchmark(get_earthquakes_async, start_date = start_date, end_date = end_date)
    assert ids == ans