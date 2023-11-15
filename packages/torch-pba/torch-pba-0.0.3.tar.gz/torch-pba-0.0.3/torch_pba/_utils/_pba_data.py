
# -- import packages: ---------------------------------------------------------
import ABCParse
import anndata
import numpy as np
import os
import pathlib

# -- set typing: --------------------------------------------------------------
from typing import List, Union


# -- Operational class: -------------------------------------------------------
class PBAData(ABCParse.ABCParse):
    def __init__(
        self,
        data_dir: Union[pathlib.Path, str],
        files: List[str] = ["R", "S", "X"],
        *args,
        **kwargs,
    ):

        self.__parse__(locals())
        self._load_files()

    def _data_path(self, file) -> str:
        return os.path.join(self.data_dir, "{}.npy".format(file))

    def _load_numpy(self, file) -> np.ndarray:
        return np.load(self._data_path(file))

    def _load_files(self) -> None:
        [setattr(self, file, self._load_numpy(file)) for file in self.files]

    def _configure_adata(self) -> None:
        if not hasattr(self, "_adata"):
            self._adata = anndata.AnnData(
                self.X, dtype=self.X.dtype, obsm={"S": self.S}, obs={"R": self.R}
            )

    @property
    def adata(self) -> anndata.AnnData:
        self._configure_adata()
        return self._adata

    def __repr__(self) -> str:
        return "PBA AnnData:\n{}".format(self.adata)
