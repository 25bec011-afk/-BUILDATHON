import streamlit as st

st.title("🎮 Advanced 3D FPS Shooter")

html_code = """
<!DOCTYPE html>
<html>
<head>
<script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"></script>
<style>
body { margin: 0; overflow: hidden; }
#crosshair {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    font-size: 24px;
    color: red;
}
</style>
</head>
<body>

<div id="crosshair">+</div>
<canvas id="game"></canvas>

<script>
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, 800/500, 0.1, 1000);

const renderer = new THREE.WebGLRenderer({canvas: document.getElementById("game")});
renderer.setSize(800, 500);

// Floor
const floorGeo = new THREE.PlaneGeometry(20,20);
const floorMat = new THREE.MeshBasicMaterial({color: 0x444444, side: THREE.DoubleSide});
const floor = new THREE.Mesh(floorGeo, floorMat);
floor.rotation.x = Math.PI/2;
scene.add(floor);

// Player position
let player = {x:0, z:5};

// Enemy
const enemyGeo = new THREE.BoxGeometry();
const enemyMat = new THREE.MeshBasicMaterial({color: 0xff0000});
const enemy = new THREE.Mesh(enemyGeo, enemyMat);
enemy.position.set(0,1,-5);
scene.add(enemy);

// Camera
camera.position.y = 2;
camera.position.z = player.z;

// Movement
document.addEventListener("keydown", (e)=>{
    if(e.key === "w") player.z -= 0.3;
    if(e.key === "s") player.z += 0.3;
    if(e.key === "a") player.x -= 0.3;
    if(e.key === "d") player.x += 0.3;
});

// Shooting
document.addEventListener("click", ()=>{
    let dx = player.x - enemy.position.x;
    let dz = player.z - enemy.position.z;

    if(Math.sqrt(dx*dx + dz*dz) < 2){
        alert("💥 Enemy Hit!");
        enemy.position.x = (Math.random()*10)-5;
        enemy.position.z = (Math.random()*-10);
    }
});

// Animate
function animate(){
    requestAnimationFrame(animate);

    // Move enemy slowly
    enemy.position.x += Math.sin(Date.now()*0.001)*0.01;

    // Update camera
    camera.position.x = player.x;
    camera.position.z = player.z;
    camera.lookAt(enemy.position);

    renderer.render(scene, camera);
}
animate();
</script>

</body>
</html>
"""

st.components.v1.html(html_code, height=520)
