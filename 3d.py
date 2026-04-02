import streamlit as st

st.title("🎮 FPS Shooter - Advanced Version")

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

// SCENE
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, 800/500, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({canvas: canvas});
renderer.setSize(800, 500);

// LIGHT
const light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(5,10,5);
scene.add(light);

// FLOOR
const floorGeo = new THREE.PlaneGeometry(30,30);
const floorMat = new THREE.MeshStandardMaterial({color: 0x444444});
const floor = new THREE.Mesh(floorGeo, floorMat);
floor.rotation.x = -Math.PI/2;
scene.add(floor);

// WALLS
function createWall(x,z){
    const wallGeo = new THREE.BoxGeometry(2,2,2);
    const wallMat = new THREE.MeshStandardMaterial({color: 0x888888});
    const wall = new THREE.Mesh(wallGeo, wallMat);
    wall.position.set(x,1,z);
    scene.add(wall);
}

// Create map
for(let i=-10;i<=10;i+=5){
    createWall(i,-10);
    createWall(i,10);
    createWall(-10,i);
    createWall(10,i);
}

// PLAYER
let player = {x:0, z:5};
let speed = 0.15;

// ENEMY
const enemyGeo = new THREE.BoxGeometry();
const enemyMat = new THREE.MeshStandardMaterial({color: 0xff0000});
const enemy = new THREE.Mesh(enemyGeo, enemyMat);
enemy.position.set(0,1,-5);
scene.add(enemy);

// CAMERA
camera.position.y = 2;

// CONTROLS
let keys = {};

document.addEventListener("keydown", (e)=>{
    keys[e.key.toLowerCase()] = true;
});

document.addEventListener("keyup", (e)=>{
    keys[e.key.toLowerCase()] = false;
});

// SHOOTING
document.addEventListener("click", ()=>{
    let dx = enemy.position.x - player.x;
    let dz = enemy.position.z - player.z;
    let distance = Math.sqrt(dx*dx + dz*dz);

    if(distance < 5){
        alert("💥 HIT!");
        enemy.position.x = (Math.random()*20)-10;
        enemy.position.z = (Math.random()*-20);
    }
});

// GAME LOOP
function animate(){
    requestAnimationFrame(animate);

    // MOVEMENT
    if(keys["w"]) player.z += speed;
    if(keys["s"]) player.z -= speed;
    if(keys["a"]) player.x -= speed;
    if(keys["d"]) player.x += speed;

    // LIMIT AREA
    player.x = Math.max(-12, Math.min(12, player.x));
    player.z = Math.max(-12, Math.min(12, player.z));

    // ENEMY MOVEMENT
    enemy.position.x += Math.sin(Date.now()*0.002) * 0.05;

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
