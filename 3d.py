import streamlit as st

st.title("🎮 3D FPS Shooter (Working)")

html_code = """
<!DOCTYPE html>
<html>
<head>
<script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"></script>
<style>
body { margin: 0; overflow: hidden; background: black; }
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
const canvas = document.getElementById("game");

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, 800/500, 0.1, 1000);

const renderer = new THREE.WebGLRenderer({canvas: canvas});
renderer.setSize(800, 500);

// LIGHT
const light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(0,10,5);
scene.add(light);

// FLOOR
const floorGeo = new THREE.PlaneGeometry(20,20);
const floorMat = new THREE.MeshStandardMaterial({color: 0x333333});
const floor = new THREE.Mesh(floorGeo, floorMat);
floor.rotation.x = -Math.PI/2;
scene.add(floor);

// PLAYER
let player = {x:0, z:5};

// ENEMY
const enemyGeo = new THREE.BoxGeometry();
const enemyMat = new THREE.MeshStandardMaterial({color: 0xff0000});
const enemy = new THREE.Mesh(enemyGeo, enemyMat);
enemy.position.set(0,1,-5);
scene.add(enemy);

// CAMERA
camera.position.y = 2;
camera.position.z = player.z;

// KEY CONTROLS
let keys = {};

document.addEventListener("keydown", (e)=>{
    keys[e.key.toLowerCase()] = true;
});

document.addEventListener("keyup", (e)=>{
    keys[e.key.toLowerCase()] = false;
});

// SHOOTING
document.addEventListener("click", ()=>{
    let dx = player.x - enemy.position.x;
    let dz = player.z - enemy.position.z;

    let dist = Math.sqrt(dx*dx + dz*dz);

    if(dist < 2){
        alert("💥 HIT!");
        enemy.position.x = (Math.random()*10)-5;
        enemy.position.z = -Math.random()*10;
    }
});

// GAME LOOP
function animate(){
    requestAnimationFrame(animate);

    // MOVEMENT
    if(keys["w"]) player.z -= 0.1;
    if(keys["s"]) player.z += 0.1;
    if(keys["a"]) player.x -= 0.1;
    if(keys["d"]) player.x += 0.1;

    // ENEMY MOVEMENT
    enemy.position.x += Math.sin(Date.now()*0.002) * 0.02;

    // CAMERA FOLLOW
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
