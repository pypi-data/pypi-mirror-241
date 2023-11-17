from pathlib import Path

__all__ = [module.name.partition(".")[0] for module in Path(__file__).parent.iterdir()]
