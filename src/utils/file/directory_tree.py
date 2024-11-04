from pathlib import Path
import json


class DirectoryTree:
    def __init__(self, root_path):
        self.root_path = root_path
        self.tree = []

    def build(self):
        self.tree = self._build_directory_tree(self.root_path)

    def _build_directory_tree(self, root_path):
        tree = []
        root = Path(root_path)
        for item in root.iterdir():
            tree_node = {}
            tree.append(tree_node)
            tree_node["label"] = item.name
            # 获取子目录相对于父目录的路径
            relative_path = item.relative_to(self.root_path)
            tree_node["path"] = str(relative_path)
            # 如果是目录，则递归构建子树
            if item.is_dir():
                tree_node["children"] = self._build_directory_tree(item)
            # 如果是文件，则直接添加到树中
            else:
                # st_size: 文件的大小，以字节为单位。
                # st_mtime: 文件的最后修改时间，以时间戳表示。
                # st_ctime: 文件的创建时间，以时间戳表示（在 Unix 系统上，这可能是指元数据的最后更改时间）。
                # st_atime: 文件的最后访问时间，以时间戳表示。
                tree_node_stat = item.stat()
                tree_node["size"] = tree_node_stat.st_size
        return tree


if __name__ == "__main__":
    current_dir = Path.cwd()  # 获取当前工作目录
    directory_tree = DirectoryTree(current_dir)
    directory_tree.build()
    # 将目录树转换为 JSON 格式
    json_tree = json.dumps(
        directory_tree.tree,
        #默认输出ASCLL码，False可以输出中文。
        ensure_ascii=False,
    )
    print(json_tree)
