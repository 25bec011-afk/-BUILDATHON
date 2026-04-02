import streamlit as st

st.title("🎮 3D Shooter Game")

html_code = """
<!DOCTYPE html>
<html>
<head>
<script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"></script>
</head>
<body>
<canvas id="game"></canvas>

<script>
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);

const renderer = new THREE.WebGLRenderer({canvas: document.getElementById("game")});
renderer.setSize(window.innerWidth, window.innerHeight);

// Player (cube)
const geometry = new THREE.BoxGeometry();
const material = new THREE.MeshBasicMaterial({color: 0x00ff00});
const player = new THREE.Mesh(geometry, material);
scene.add(player);

// Enemy
const enemyGeo = new THREE.BoxGeometry();
const enemyMat = new THREE.MeshBasicMaterial({color: 0xff0000});
const enemy = new THREE.Mesh(enemyGeo, enemyMat);
enemy.position.x = 3;
scene.add(enemy);

camera.position.z = 5;

// Movement
document.addEventListener("keydown", (e)=>{
    if(e.key === "ArrowLeft") player.position.x -= 0.2;
    if(e.key === "ArrowRight") player.position.x += 0.2;
});

// Shooting
document.addEventListener("click", ()=>{
    if(Math.abs(player.position.x - enemy.position.x) < 1){
        enemy.position.x = Math.random()*6 - 3;
        alert("💥 Hit!");
    }
});

function animate(){
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}
animate();
</script>

</body>
</html>
"""

st.components.v1.html(html_code, height=600)
