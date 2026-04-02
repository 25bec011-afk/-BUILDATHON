import streamlit as st

st.title("🎮 Large 3D TPS Game Engine")

html_code = """
<!DOCTYPE html>
<html>
<head>
<script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"></script>
<style>
body { margin:0; overflow:hidden; background:black; }
</style>
</head>
<body>

<canvas id="game"></canvas>

<script>

// ================== CORE ENGINE ==================
let scene, camera, renderer;
let player, enemies = [];
let keys = {};

init();
animate();

// ================== INIT ==================
function init(){

    scene = new THREE.Scene();

    camera = new THREE.PerspectiveCamera(75, 800/500, 0.1, 1000);

    renderer = new THREE.WebGLRenderer({canvas: document.getElementById("game")});
    renderer.setSize(800, 500);

    // LIGHT
    const light = new THREE.DirectionalLight(0xffffff, 1);
    light.position.set(10,10,10);
    scene.add(light);

    createMap();
    createPlayer();
    spawnEnemies();

    setupControls();
}

// ================== MAP ==================
function createMap(){
    const groundGeo = new THREE.PlaneGeometry(100,100);
    const groundMat = new THREE.MeshStandardMaterial({color: 0x222222});
    const ground = new THREE.Mesh(groundGeo, groundMat);
    ground.rotation.x = -Math.PI/2;
    scene.add(ground);
}

// ================== PLAYER ==================
function createPlayer(){
    const geo = new THREE.BoxGeometry(1,2,1);
    const mat = new THREE.MeshStandardMaterial({color: 0x00ff00});
    player = new THREE.Mesh(geo, mat);
    player.position.y = 1;
    scene.add(player);
}

// ================== ENEMIES ==================
function spawnEnemies(){
    for(let i=0;i<5;i++){
        const geo = new THREE.BoxGeometry(1,2,1);
        const mat = new THREE.MeshStandardMaterial({color: 0xff0000});
        const enemy = new THREE.Mesh(geo, mat);
        enemy.position.set(Math.random()*20-10,1,Math.random()*-20);
        scene.add(enemy);
        enemies.push(enemy);
    }
}

// ================== CONTROLS ==================
function setupControls(){
    document.addEventListener("keydown", e=> keys[e.key.toLowerCase()] = true);
    document.addEventListener("keyup", e=> keys[e.key.toLowerCase()] = false);

    document.addEventListener("click", shoot);
}

// ================== SHOOT ==================
function shoot(){
    enemies.forEach((enemy, index)=>{
        let dist = player.position.distanceTo(enemy.position);

        if(dist < 5){
            scene.remove(enemy);
            enemies.splice(index,1);
            spawnEnemies(); // respawn
        }
    });
}

// ================== PLAYER MOVEMENT ==================
function updatePlayer(){
    let speed = 0.15;

    if(keys["w"]) player.position.z -= speed;
    if(keys["s"]) player.position.z += speed;
    if(keys["a"]) player.position.x -= speed;
    if(keys["d"]) player.position.x += speed;
}

// ================== ENEMY AI ==================
function updateEnemies(){
    enemies.forEach(enemy=>{
        // move toward player
        let dx = player.position.x - enemy.position.x;
        let dz = player.position.z - enemy.position.z;

        enemy.position.x += dx * 0.005;
        enemy.position.z += dz * 0.005;
    });
}

// ================== CAMERA ==================
function updateCamera(){
    camera.position.x = player.position.x;
    camera.position.y = player.position.y + 5;
    camera.position.z = player.position.z + 8;

    camera.lookAt(player.position);
}

// ================== GAME LOOP ==================
function animate(){
    requestAnimationFrame(animate);

    updatePlayer();
    updateEnemies();
    updateCamera();

    renderer.render(scene, camera);
}

</script>

</body>
</html>
"""

st.components.v1.html(html_code, height=520)
