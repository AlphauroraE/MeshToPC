# MeshToPC

This code utilizes the [Open3D](http://www.open3d.org/) and [OS](https://docs.python.org/3/library/os.html) libraries to convert a folder of triangle meshes to a corresponding folder of point clouds (.pcd files).

It computes vertex normals and then samples points uniformly. The output point clouds are named based on the file name of the mesh. The function call defaults to a point density of 5000, but this may be adjusted as desired. Finally, the resulting point cloud(s) are displayed in a window.
