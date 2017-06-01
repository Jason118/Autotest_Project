
import time
import pytest


if __name__ == '__main__':
    # args = ['-q', '-s']
    # pytest.main(args)
    now_time = time.strftime("%Y%m%d", time.localtime(time.time()))
    args = ['--html=../../../report/interface_autotest_report_%s.html' % now_time]
    # args = ['--html=./interface_autotest_report_%s.html' % now_time]
    pytest.main(args)