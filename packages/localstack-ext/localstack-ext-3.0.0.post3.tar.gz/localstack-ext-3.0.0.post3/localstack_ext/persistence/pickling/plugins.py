from localstack.runtime import hooks
@hooks.on_infra_start()
def register_pickle_patches_runtime():from.reducers import register as A;A()