
# Some old code using fixtures to clean up tmp test dirs and files:

# CURR_PATH = Path(__file__).parent.resolve()
# TEST_PATH = CURR_PATH / 'tmp'


# @pytest.fixture(scope='package', autouse=True)
# def package_setup():
#     # This is invoked just before the first test in this package runs.
#     if TEST_PATH.exists():
#         shutil.rmtree(TEST_PATH)
#     TEST_PATH.mkdir()
#     os.chdir(TEST_PATH)


# @pytest.fixture(scope='package', autouse=True)
# def package_teardown():
#     yield
#     os.chdir(CURR_PATH)
#     if TEST_PATH.exists():
#        shutil.rmtree(TEST_PATH)
