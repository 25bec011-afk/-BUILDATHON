import streamlit as st

st.title("🎮 Real FPS Shooter")

html_code = """
<!DOCTYPE html>
<html>
<head>
<script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.152.2/examples/js/controls/PointerLockControls.js"></script>
<style>
body { margin:0; overflow:hidden; background:black; }
#info {
    position:absolute;
    top:40%;
    width:100%;
    text-align:center;
    color:white;
    font-size:20px;
}
</style>
</head>
<body>

<div id="info">Click to start FPS mode</div>
<canvas id="game"></canvas>

<script>
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x202020);

const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);

const renderer = new THREE.WebGLRenderer({canvas: document.getElementById("game")});
renderer.setSize(window.innerWidth, 500);

// LIGHT
const light = new THREE.HemisphereLight(0xffffff, 0x444444);
scene.add(light);

// FLOOR
const floor = new THREE.Mesh(
    new THREE.PlaneGeometry(100,100),
    new THREE.MeshStandardMaterial({color:0x333333})
);
floor.rotation.x = -Math.PI/2;
scene.add(floor);

// PLAYER CONTROLS (REAL FPS)
const controls = new THREE.PointerLockControls(camera, document.body);

document.getElementById("info").addEventListener("click", ()=>{
    controls.lock();
});

// MOVEMENT
let move = {forward:false, back:false, left:false, right:false};

document.addEventListener("keydown", e=>{
    if(e.code==="KeyW") move.forward=true;
    if(e.code==="KeyS") move.back=true;
    if(e.code==="KeyA") move.left=true;
    if(e.code==="KeyD") move.right=true;
});

document.addEventListener("keyup", e=>{
    if(e.code==="KeyW") move.forward=false;
    if(e.code==="KeyS") move.back=false;
    if(e.code==="KeyA") move.left=false;
    if(e.code==="KeyD") move.right=false;
});

// ENEMIES
let enemies = [];

function createEnemy(){
    const e = new THREE.Mesh(
        new THREE.BoxGeometry(),
        new THREE.MeshStandardMaterial({color:0xff0000})
    );
    e.position.set(Math.random()*20-10,1,Math.random()*-20);
    scene.add(e);
    enemies.push(e);
}

for(let i=0;i<5;i++) createEnemy();

// SHOOT (REAL AIM USING RAYCAST)
const raycaster = new THREE.Raycaster();

document.addEventListener("click", ()=>{
    raycaster.setFromCamera(new THREE.Vector2(0,0), camera);

    const hits = raycaster.intersectObjects(enemies);

    if(hits.length > 0){
        let hit = hits[0].object;
        scene.remove(hit);
        enemies = enemies.filter(e => e !== hit);
        createEnemy();
    }
});

// GAME LOOP
function animate(){
    requestAnimationFrame(animate);

    let speed = 0.1;

    if(move.forward) controls.moveForward(speed);
    if(move.back) controls.moveForward(-speed);
    if(move.left) controls.moveRight(-speed);
    if(move.right) controls.moveRight(speed);

    renderer.render(scene, camera);
}

animate();
</script>

</body>
</html>
"""

st.components.v1.html(html_code, height=520)
