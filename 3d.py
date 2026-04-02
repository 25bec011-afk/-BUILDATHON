import streamlit as st

st.title("🧱 Mini Minecraft FPS")

html_code = """
<!DOCTYPE html>
<html>
<head>
<script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"></script>
<style>
body { margin:0; overflow:hidden; background:black; }
#crosshair {
    position:absolute;
    top:50%; left:50%;
    transform:translate(-50%,-50%);
    color:white;
    font-size:20px;
}
</style>
</head>
<body>

<div id="crosshair">+</div>
<canvas id="game"></canvas>

<script>
const canvas = document.getElementById("game");

// Scene
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x87CEEB);

// Camera (player)
const camera = new THREE.PerspectiveCamera(75, 800/500, 0.1, 1000);

// Renderer
const renderer = new THREE.WebGLRenderer({canvas: canvas});
renderer.setSize(800,500);

// Light
const light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(5,10,5);
scene.add(light);

// Ground
const groundGeo = new THREE.PlaneGeometry(50,50);
const groundMat = new THREE.MeshStandardMaterial({color: 0x228B22});
const ground = new THREE.Mesh(groundGeo, groundMat);
ground.rotation.x = -Math.PI/2;
scene.add(ground);

// Blocks (Minecraft style)
let blocks = [];

function createBlock(x,y,z){
    const geo = new THREE.BoxGeometry();
    const mat = new THREE.MeshStandardMaterial({color: 0x8B4513});
    const block = new THREE.Mesh(geo, mat);
    block.position.set(x,y,z);
    scene.add(block);
    blocks.push(block);
}

// Create random blocks
for(let i=0;i<20;i++){
    createBlock(Math.random()*20-10,1,Math.random()*-20);
}

// Player position
let player = {x:0, y:2, z:5};
camera.position.set(player.x, player.y, player.z);

// Controls
let keys = {};
document.addEventListener("keydown", e => keys[e.key.toLowerCase()] = true);
document.addEventListener("keyup", e => keys[e.key.toLowerCase()] = false);

// Mouse look
let yaw = 0;
document.addEventListener("mousemove", e=>{
    yaw -= e.movementX * 0.002;
});

// Shoot (remove block)
document.addEventListener("click", ()=>{
    blocks.forEach((b, i)=>{
        let dist = camera.position.distanceTo(b.position);
        if(dist < 3){
            scene.remove(b);
            blocks.splice(i,1);
        }
    });
});

// Game loop
function animate(){
    requestAnimationFrame(animate);

    let speed = 0.1;

    if(keys["w"]) player.z -= speed;
    if(keys["s"]) player.z += speed;
    if(keys["a"]) player.x -= speed;
    if(keys["d"]) player.x += speed;

    camera.position.set(player.x, player.y, player.z);

    camera.rotation.y = yaw;

    renderer.render(scene, camera);
}

animate();
</script>

</body>
</html>
"""

st.components.v1.html(html_code, height=520)
