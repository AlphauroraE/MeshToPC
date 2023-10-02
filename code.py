import os
import open3d as o3d

def mesh_to_pc(inputpath, meshpath,points,outputname,outputpath):
    """"Convert a folder of meshes into a folder of corresponding point clouds"""
    mesh = o3d.io.read_triangle_mesh(meshpath) # Looks at the mesh
    mesh.compute_vertex_normals()
    pcd = mesh.sample_points_uniformly(number_of_points = points) # Uniformly samples however many points on the mesh surface to make a point cloud
    os.chdir(outputpath) # move into the output folder
    o3d.io.write_point_cloud(outputname,pcd) # create a file storing the point cloud in the output folder
    os.chdir(inputpath) # move back to the input folder to prepare for the next function call

#TODO: Change inputpath depending on the computer
inputpath = "..." # The path to the input folder on computer (change depending on computer)
os.chdir(inputpath) # move into the input folder
# path = os.getcwd() # get the current working directory (current folder, aka input folder)
# dir_list = os.listdir(path) # makes a list of the names of the files in my input folder

#TODO: Change parent_dir depending on the computer
parent_dir = "..." # This is the place (larger folder) where I want to store my new output folder
directory = input("What to name the output folder? ") # take user input for what to name the output folder
outputpath = os.path.join(parent_dir, directory) # combines the two together to make a path to the output folder
os.mkdir(outputpath) # makes the output folder. now we have a place to store our point clouds!

obj = os.scandir(os.getcwd())
for entry in obj: # goes through the input folder
    inputfile = entry.name
    if inputfile != ".DS_Store": # The first entry was always .DS_Store, and this is not a mesh file
        if inputfile.find("_") != -1: # mesh files without underscore were returning -1 and creating a name cut off letters
            newname = inputfile.replace(inputfile[inputfile.find("_"):],"") # basically removes everything after underscore
        else:
            newname = inputfile[:inputfile.find(".ply")] # new name is everything up to the file type specification
        outputfile = newname + ".pcd" # this is the name for the output file of this point cloud
        mesh_to_pc(inputpath,inputfile,5000,outputfile,outputpath) # call the function defined above

os.chdir(outputpath)
obj = os.scandir(os.getcwd())
for entry in obj:
    if entry.name != ".DS_Store":
        pcdpath = entry.name # path to the point cloud
        displaypcd = o3d.io.read_point_cloud(pcdpath) # reading the point cloud
        o3d.visualization.draw_geometries([displaypcd]) #displaying the point cloud by calling draw_geometries
