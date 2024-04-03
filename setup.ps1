git submodule update --init

$files = Get-ChildItem -Path "./models"

New-Item -Path "./yolov5/" -Name "runs" -ItemType "directory" 
New-Item -Path "./yolov5/runs" -Name "train" -ItemType "directory" 


for ($i = 0; $i -lt $files.length; $i++) {
    Copy-Item -path $files[$i].FullName -Recurse -Destination "./yolov5/runs/train"
}