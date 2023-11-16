// SampleFromVoxels.h
// Copyright Contributors to the OpenVDB Project
// SPDX-License-Identifier: MPL-2.0

//////////////////////////////////////////////////////////////////////////
///
/// @file SampleFromVoxels.h
///
/// @brief NearestNeighborSampler, TrilinearSampler, TriquadraticSampler and TricubicSampler
///
/// @note These interpolators employ internal caching for better performance when used repeatedly
///       in the same voxel location, so try to reuse an instance of these classes more than once.
///
/// @warning While all the interpolators defined below work with both scalars and vectors
///          values (e.g. float and Vec3<float>) TrilinarSampler::zeroCrossing and
///          Trilinear::gradient will only compile with floating point value types.
///
/// @author Ken Museth
///
///////////////////////////////////////////////////////////////////////////

#ifndef NANOVDB_SAMPLE_FROM_VOXELS_H_HAS_BEEN_INCLUDED
#define NANOVDB_SAMPLE_FROM_VOXELS_H_HAS_BEEN_INCLUDED

// Only define __hostdev__ when compiling as NVIDIA CUDA
#ifdef __CUDACC__
#define __hostdev__ __host__ __device__
#elif defined(__KERNEL_METAL__)
#else
#include <cmath> // for floor
#define __hostdev__
#endif

namespace nanovdb {

// Forward declaration of sampler with specific polynomial orders
template<typename TreeT, int Order, bool UseCache = true>
class SampleFromVoxels;

/// @brief Factory free-function for a sampler of specific polynomial orders
///
/// @details This allows for the compact syntax:
/// @code
///   auto acc = grid.getAccessor();
///   auto smp = nanovdb::createSampler<1>( acc );
/// @endcode
template<int Order, typename TreeOrAccT, bool UseCache = true>
__hostdev__ SampleFromVoxels<TreeOrAccT, Order, UseCache> createSampler(__global__ const TreeOrAccT& acc)
{
    return SampleFromVoxels<TreeOrAccT, Order, UseCache>(acc);
}

/// @brief Utility function that returns the Coord of the round-down of @a xyz
///        and redefined @xyz as the fractional part, ie xyz-in = return-value + xyz-out
template<typename CoordT, typename RealT, template<typename> class Vec3T>
__hostdev__ inline CoordT Floor(__global__ Vec3T<RealT>& xyz);

/// @brief Template specialization of Floor for Vec3<float>
template<typename CoordT, template<typename> class Vec3T>
__hostdev__ inline CoordT Floor(__global__ Vec3T<float>& xyz)
{
    const float ijk[3] = {floorf(xyz[0]), floorf(xyz[1]), floorf(xyz[2])};
    xyz[0] -= ijk[0];
    xyz[1] -= ijk[1];
    xyz[2] -= ijk[2];
    return CoordT(int32_t(ijk[0]), int32_t(ijk[1]), int32_t(ijk[2]));
}

/// @brief Template specialization of Floor for Vec3<float>
template<typename CoordT, template<typename> class Vec3T>
__hostdev__ inline CoordT Floor(__global__ Vec3T<double>& xyz)
{
    const double ijk[3] = {floor(xyz[0]), floor(xyz[1]), floor(xyz[2])};
    xyz[0] -= ijk[0];
    xyz[1] -= ijk[1];
    xyz[2] -= ijk[2];
    return CoordT(int32_t(ijk[0]), int32_t(ijk[1]), int32_t(ijk[2]));
}

#if defined(__KERNEL_METAL__)
/// @brief Template specialization of Floor for Vec3<float>
template<typename CoordT, template<typename> class Vec3T>
__hostdev__ inline CoordT Floor(__local__ Vec3T<float>& xyz)
{
    const float ijk[3] = {floorf(xyz[0]), floorf(xyz[1]), floorf(xyz[2])};
    xyz[0] -= ijk[0];
    xyz[1] -= ijk[1];
    xyz[2] -= ijk[2];
    return CoordT(int32_t(ijk[0]), int32_t(ijk[1]), int32_t(ijk[2]));
}

/// @brief Template specialization of Floor for Vec3<float>
template<typename CoordT, template<typename> class Vec3T>
__hostdev__ inline CoordT Floor(__local__ Vec3T<double>& xyz)
{
    const double ijk[3] = {floor(xyz[0]), floor(xyz[1]), floor(xyz[2])};
    xyz[0] -= ijk[0];
    xyz[1] -= ijk[1];
    xyz[2] -= ijk[2];
    return CoordT(int32_t(ijk[0]), int32_t(ijk[1]), int32_t(ijk[2]));
}
#endif

// ------------------------------> NearestNeighborSampler <--------------------------------------

/// @brief Nearest neighbor, i.e. zero order, interpolator with caching
template<typename TreeOrAccT>
class SampleFromVoxels<TreeOrAccT, 0, true>
{
public:
    using ValueT = typename TreeOrAccT::ValueType;
    using CoordT = typename TreeOrAccT::CoordType;

    static __constant__ const int ORDER = 0;
    /// @brief Construction from a Tree or ReadAccessor
    __hostdev__ SampleFromVoxels(__local__ const TreeOrAccT& acc)
        : mAcc(acc)
        , mPos(CoordT::max())
    {
    }

    __hostdev__ __global__ const TreeOrAccT& accessor() const { return mAcc; }

    /// @note xyz is in index space space
    template<typename Vec3T>
    inline __hostdev__ ValueT operator()(__global__ const Vec3T& xyz) const __local__;
#if defined(__KERNEL_METAL__)
    template<typename Vec3T>
    inline __hostdev__ ValueT operator()(__local__ const Vec3T& xyz) const __local__;
#endif

    inline __hostdev__ ValueT operator()(__global__ const CoordT& ijk) const __local__;

    inline __hostdev__ ValueT operator()() const;

private:
    __global__ const TreeOrAccT& mAcc;
    mutable CoordT    mPos;
    mutable ValueT    mVal; // private cache
}; // SampleFromVoxels<TreeOrAccT, 0, true>

/// @brief Nearest neighbor, i.e. zero order, interpolator without caching
template<typename TreeOrAccT>
class SampleFromVoxels<TreeOrAccT, 0, false>
{
public:
    using ValueT = typename TreeOrAccT::ValueType;
    using CoordT = typename TreeOrAccT::CoordType;
    static __constant__ const int ORDER = 0;

    /// @brief Construction from a Tree or ReadAccessor
    __hostdev__ SampleFromVoxels(__local__ const TreeOrAccT& acc)
        : mAcc(acc)
    {
    }

    __hostdev__ __global__ const TreeOrAccT& accessor() const __local__ { return mAcc; }

    /// @note xyz is in index space space
    template<typename Vec3T>
    inline __hostdev__ ValueT operator()(__global__ const Vec3T& xyz) const __local__;
#if defined(__KERNEL_METAL__)
    template<typename Vec3T>
    inline __hostdev__ ValueT operator()(__local__ const Vec3T& xyz) const __local__;
#endif

    inline __hostdev__ ValueT operator()(__global__ const CoordT& ijk) const __local__ { return mAcc.getValue(ijk);}

private:
    __local__ const TreeOrAccT& mAcc;
}; // SampleFromVoxels<TreeOrAccT, 0, false>

template<typename TreeOrAccT>
template<typename Vec3T>
typename TreeOrAccT::ValueType SampleFromVoxels<TreeOrAccT, 0, true>::operator()(__global__ const Vec3T& xyz) const __local__
{
    const CoordT ijk = Round<CoordT>(xyz);
    if (ijk != mPos) {
        mPos = ijk;
        mVal = mAcc.getValue(mPos);
    }
    return mVal;
}
#if defined(__KERNEL_METAL__)
template<typename TreeOrAccT>
template<typename Vec3T>
typename TreeOrAccT::ValueType SampleFromVoxels<TreeOrAccT, 0, true>::operator()(__local__ const Vec3T& xyz) const __local__
{
    const CoordT ijk = Round<CoordT>(xyz);
    if (ijk != mPos) {
        mPos = ijk;
        mVal = mAcc.getValue(mPos);
    }
    return mVal;
}
#endif

template<typename TreeOrAccT>
typename TreeOrAccT::ValueType SampleFromVoxels<TreeOrAccT, 0, true>::operator()(__global__ const CoordT& ijk) const __local__
{
    if (ijk != mPos) {
        mPos = ijk;
        mVal = mAcc.getValue(mPos);
    }
    return mVal;
}

template<typename TreeOrAccT>
template<typename Vec3T>
typename TreeOrAccT::ValueType SampleFromVoxels<TreeOrAccT, 0, false>::operator()(__global__ const Vec3T& xyz) const __local__
{
    return mAcc.getValue(Round<CoordT>(xyz));
}

#if defined(__KERNEL_METAL__)
template<typename TreeOrAccT>
template<typename Vec3T>
typename TreeOrAccT::ValueType SampleFromVoxels<TreeOrAccT, 0, false>::operator()(__local__ const Vec3T& xyz) const __local__
{
    return mAcc.getValue(Round<CoordT>(xyz));
}
#endif

// ------------------------------> TrilinearSampler <--------------------------------------

/// @brief Tri-linear sampler, i.e. first order, interpolator
template<typename TreeOrAccT>
class TrilinearSampler
{
#if defined(__KERNEL_METAL__)
public:
#else
protected:
#endif
    __local__ const TreeOrAccT& mAcc;

public:
    using ValueT = typename TreeOrAccT::ValueType;
    using CoordT = typename TreeOrAccT::CoordType;
    static __constant__ const int ORDER = 1;

    /// @brief Protected constructor from a Tree or ReadAccessor
    __hostdev__ TrilinearSampler(__local__ const TreeOrAccT& acc) : mAcc(acc) {}

    __hostdev__ __global__ const TreeOrAccT& accessor() const { return mAcc; }

    /// @brief Extract the stencil of 8 values
    inline __hostdev__ void stencil(__global__ CoordT& ijk, __global__ ValueT (&v)[2][2][2]) const;

    template<typename RealT, template<typename...> class Vec3T>
    static inline __hostdev__ ValueT sample(__global__ const Vec3T<RealT> &uvw, __global__ const ValueT (&v)[2][2][2]);

    template<typename RealT, template<typename...> class Vec3T>
    static inline __hostdev__ Vec3T<ValueT> gradient(__global__ const Vec3T<RealT> &uvw, __global__ const ValueT (&v)[2][2][2]);

    static inline __hostdev__ bool zeroCrossing(__global__ const ValueT (&v)[2][2][2]);
}; // TrilinearSamplerBase

template<typename TreeOrAccT>
void TrilinearSampler<TreeOrAccT>::stencil(__global__ CoordT& ijk, __global__ ValueT (&v)[2][2][2]) const
{
    v[0][0][0] = mAcc.getValue(ijk); // i, j, k

    ijk[2] += 1;
    v[0][0][1] = mAcc.getValue(ijk); // i, j, k + 1

    ijk[1] += 1;
    v[0][1][1] = mAcc.getValue(ijk); // i, j+1, k + 1

    ijk[2] -= 1;
    v[0][1][0] = mAcc.getValue(ijk); // i, j+1, k

    ijk[0] += 1;
    ijk[1] -= 1;
    v[1][0][0] = mAcc.getValue(ijk); // i+1, j, k

    ijk[2] += 1;
    v[1][0][1] = mAcc.getValue(ijk); // i+1, j, k + 1

    ijk[1] += 1;
    v[1][1][1] = mAcc.getValue(ijk); // i+1, j+1, k + 1

    ijk[2] -= 1;
    v[1][1][0] = mAcc.getValue(ijk); // i+1, j+1, k
}

template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
typename TreeOrAccT::ValueType TrilinearSampler<TreeOrAccT>::sample(__global__ const Vec3T<RealT> &uvw, __global__ const ValueT (&v)[2][2][2])
{
#if 0
  auto lerp = [](ValueT a, ValueT b, ValueT w){ return fma(w, b-a, a); };// = w*(b-a) + a
  //auto lerp = [](ValueT a, ValueT b, ValueT w){ return fma(w, b, fma(-w, a, a));};// = (1-w)*a + w*b
#else
  struct Lerp {
    static ValueT lerp(ValueT a, ValueT b, RealT w) { return a + ValueT(w) * (b - a); }
  };
#endif
    return Lerp::lerp(Lerp::lerp(Lerp::lerp(v[0][0][0], v[0][0][1], uvw[2]), Lerp::lerp(v[0][1][0], v[0][1][1], uvw[2]), uvw[1]),
        Lerp::lerp(Lerp::lerp(v[1][0][0], v[1][0][1], uvw[2]), Lerp::lerp(v[1][1][0], v[1][1][1], uvw[2]), uvw[1]),
                uvw[0]);
}

template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
Vec3T<typename TreeOrAccT::ValueType> TrilinearSampler<TreeOrAccT>::gradient(__global__ const Vec3T<RealT> &uvw, __global__ const ValueT (&v)[2][2][2])
{
    static_assert(is_floating_point<ValueT>::value, "TrilinearSampler::gradient requires a floating-point type");
#if 0
  auto lerp = [](ValueT a, ValueT b, ValueT w){ return fma(w, b-a, a); };// = w*(b-a) + a
  //auto lerp = [](ValueT a, ValueT b, ValueT w){ return fma(w, b, fma(-w, a, a));};// = (1-w)*a + w*b
#else
  struct Lerp {
    static ValueT lerp(ValueT a, ValueT b, RealT w) { return a + ValueT(w) * (b - a); }
  };
#endif

    ValueT D[4] = {v[0][0][1] - v[0][0][0], v[0][1][1] - v[0][1][0], v[1][0][1] - v[1][0][0], v[1][1][1] - v[1][1][0]};

    // Z component
    Vec3T<ValueT> grad(0, 0, Lerp::lerp(Lerp::lerp(D[0], D[1], uvw[1]), lerp(D[2], D[3], uvw[1]), uvw[0]));

    const ValueT w = ValueT(uvw[2]);
    D[0] = v[0][0][0] + D[0] * w;
    D[1] = v[0][1][0] + D[1] * w;
    D[2] = v[1][0][0] + D[2] * w;
    D[3] = v[1][1][0] + D[3] * w;

    // X component
    grad[0] = Lerp::lerp(D[2], D[3], uvw[1]) - Lerp::lerp(D[0], D[1], uvw[1]);

    // Y component
    grad[1] = Lerp::lerp(D[1] - D[0], D[3] - D[2], uvw[0]);

    return grad;
}

template<typename TreeOrAccT>
bool TrilinearSampler<TreeOrAccT>::zeroCrossing(__global__ const ValueT (&v)[2][2][2])
{
    static_assert(is_floating_point<ValueT>::value, "TrilinearSampler::zeroCrossing requires a floating-point type");
    const bool less = v[0][0][0] < ValueT(0);
    return (less ^ (v[0][0][1] < ValueT(0))) ||
           (less ^ (v[0][1][1] < ValueT(0))) ||
           (less ^ (v[0][1][0] < ValueT(0))) ||
           (less ^ (v[1][0][0] < ValueT(0))) ||
           (less ^ (v[1][0][1] < ValueT(0))) ||
           (less ^ (v[1][1][1] < ValueT(0))) ||
           (less ^ (v[1][1][0] < ValueT(0)));
}

/// @brief Template specialization that does not use caching of stencil points
template<typename TreeOrAccT>
class SampleFromVoxels<TreeOrAccT, 1, false>
#if !defined(__KERNEL_METAL__)
    : public TrilinearSampler<TreeOrAccT>
#endif
{
#if defined(__KERNEL_METAL__)

    TrilinearSampler<TreeOrAccT> _base;
#define BASE(v) _base.v
#else
#define BASE(v) BaseT::v

#endif
    using BaseT = TrilinearSampler<TreeOrAccT>;
    using ValueT = typename TreeOrAccT::ValueType;
    using CoordT = typename TreeOrAccT::CoordType;

public:

    /// @brief Construction from a Tree or ReadAccessor
#if defined(__KERNEL_METAL__)
    __hostdev__ SampleFromVoxels(__local__ const TreeOrAccT& acc) : _base(acc) {}
#else
    __hostdev__ SampleFromVoxels(__local__ const TreeOrAccT& acc) : BaseT(acc) {}
#endif

    /// @note xyz is in index space space
    template<typename RealT, template<typename...> class Vec3T>
    inline __hostdev__ ValueT operator()(Vec3T<RealT> xyz) const;

    /// @note ijk is in index space space
    __hostdev__ ValueT operator()(__global__ const CoordT &ijk) const {return BaseT::mAcc.getValue(ijk);}

    /// @brief Return the gradient in index space.
    ///
    /// @warning Will only compile with floating point value types
    template<typename RealT, template<typename...> class Vec3T>
    inline __hostdev__ Vec3T<ValueT> gradient(Vec3T<RealT> xyz) const;

    /// @brief Return true if the tr-linear stencil has a zero crossing at the specified index position.
    ///
    /// @warning Will only compile with floating point value types
    template<typename RealT, template<typename...> class Vec3T>
    inline __hostdev__ bool zeroCrossing(Vec3T<RealT> xyz) const;

}; // SampleFromVoxels<TreeOrAccT, 1, false>

/// @brief Template specialization with caching of stencil values
template<typename TreeOrAccT>
class SampleFromVoxels<TreeOrAccT, 1, true>
#if !defined(__KERNEL_METAL__)
    : public TrilinearSampler<TreeOrAccT>
#endif
{
#if defined(__KERNEL_METAL__)
    TrilinearSampler<TreeOrAccT> _base;
#endif
    using BaseT = TrilinearSampler<TreeOrAccT>;
    using ValueT = typename TreeOrAccT::ValueType;
    using CoordT = typename TreeOrAccT::CoordType;

    mutable CoordT mPos;
    mutable ValueT mVal[2][2][2];

    template<typename RealT, template<typename...> class Vec3T>
    __hostdev__ void cache(__global__ Vec3T<RealT>& xyz) const;
public:

    /// @brief Construction from a Tree or ReadAccessor
    __hostdev__ SampleFromVoxels(__local__ const TreeOrAccT& acc) : BaseT(acc), mPos(CoordT::max()){}

    /// @note xyz is in index space space
    template<typename RealT, template<typename...> class Vec3T>
    inline __hostdev__ ValueT operator()(Vec3T<RealT> xyz) const;

    // @note ijk is in index space space
    __hostdev__ ValueT operator()(__global__ const CoordT &ijk) const;

    /// @brief Return the gradient in index space.
    ///
    /// @warning Will only compile with floating point value types
    template<typename RealT, template<typename...> class Vec3T>
    inline __hostdev__ Vec3T<ValueT> gradient(Vec3T<RealT> xyz) const;

    /// @brief Return true if the tr-linear stencil has a zero crossing at the specified index position.
    ///
    /// @warning Will only compile with floating point value types
    template<typename RealT, template<typename...> class Vec3T>
    inline __hostdev__ bool zeroCrossing(Vec3T<RealT> xyz) const;

    /// @brief Return true if the cached tri-linear stencil has a zero crossing.
    ///
    /// @warning Will only compile with floating point value types
    __hostdev__ bool zeroCrossing() const { return BaseT::zeroCrossing(mVal); }

}; // SampleFromVoxels<TreeOrAccT, 1, true>

template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
typename TreeOrAccT::ValueType SampleFromVoxels<TreeOrAccT, 1, true>::operator()(Vec3T<RealT> xyz) const
{
    this->cache(xyz);
    return BaseT::sample(xyz, mVal);
}

template<typename TreeOrAccT>
typename TreeOrAccT::ValueType SampleFromVoxels<TreeOrAccT, 1, true>::operator()(__global__ const CoordT &ijk) const
{
    return  ijk == mPos ? mVal[0][0][0] : BaseT::mAcc.getValue(ijk);
}

template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
Vec3T<typename TreeOrAccT::ValueType> SampleFromVoxels<TreeOrAccT, 1, true>::gradient(Vec3T<RealT> xyz) const
{
    this->cache(xyz);
    return BaseT::gradient(xyz, mVal);
}

template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
__hostdev__ bool SampleFromVoxels<TreeOrAccT, 1, true>::zeroCrossing(Vec3T<RealT> xyz) const
{
    this->cache(xyz);
    return BaseT::zeroCrossing(mVal);
}

template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
void SampleFromVoxels<TreeOrAccT, 1, true>::cache(__global__ Vec3T<RealT>& xyz) const
{
    CoordT ijk = Floor<CoordT>(xyz);
    if (ijk != mPos) {
        mPos = ijk;
        BaseT::stencil(ijk, mVal);
    }
}

#if 0

template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
typename TreeOrAccT::ValueType SampleFromVoxels<TreeOrAccT, 1, false>::operator()(Vec3T<RealT> xyz) const
{
    ValueT val[2][2][2];
    CoordT ijk = Floor<CoordT>(xyz);
    BaseT::stencil(ijk, val);
    return BaseT::sample(xyz, val);
}

#else

template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
typename TreeOrAccT::ValueType SampleFromVoxels<TreeOrAccT, 1, false>::operator()(Vec3T<RealT> xyz) const
{
    struct Lerp {
        static ValueT lerp(ValueT a, ValueT b, RealT w) { return a + ValueT(w) * (b - a); }
    };

    CoordT coord = Floor<CoordT>(xyz);

    ValueT vx, vx1, vy, vy1, vz, vz1;

    vz = BASE(mAcc).getValue(coord);
    coord[2] += 1;
    vz1 = BASE(mAcc).getValue(coord);
    vy = Lerp::lerp(vz, vz1, xyz[2]);

    coord[1] += 1;

    vz1 = BASE(mAcc).getValue(coord);
    coord[2] -= 1;
    vz = BASE(mAcc).getValue(coord);
    vy1 = Lerp::lerp(vz, vz1, xyz[2]);

    vx = Lerp::lerp(vy, vy1, xyz[1]);

    coord[0] += 1;

    vz = BASE(mAcc).getValue(coord);
    coord[2] += 1;
    vz1 = BASE(mAcc).getValue(coord);
    vy1 = Lerp::lerp(vz, vz1, xyz[2]);

    coord[1] -= 1;

    vz1 = BASE(mAcc).getValue(coord);
    coord[2] -= 1;
    vz = BASE(mAcc).getValue(coord);
    vy = Lerp::lerp(vz, vz1, xyz[2]);

    vx1 = Lerp::lerp(vy, vy1, xyz[1]);

    return Lerp::lerp(vx, vx1, xyz[0]);
}
#endif


template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
inline Vec3T<typename TreeOrAccT::ValueType> SampleFromVoxels<TreeOrAccT, 1, false>::gradient(Vec3T<RealT> xyz) const
{
    ValueT val[2][2][2];
    CoordT ijk = Floor<CoordT>(xyz);
    BaseT::stencil(ijk, val);
    return BaseT::gradient(xyz, val);
}

template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
bool SampleFromVoxels<TreeOrAccT, 1, false>::zeroCrossing(Vec3T<RealT> xyz) const
{
    ValueT val[2][2][2];
    CoordT ijk = Floor<CoordT>(xyz);
    BaseT::stencil(ijk, val);
    return BaseT::zeroCrossing(val);
}

// ------------------------------> TriquadraticSampler <--------------------------------------

/// @brief Tri-quadratic sampler, i.e. second order, interpolator
template<typename TreeOrAccT>
class TriquadraticSampler
{
protected:
    __local__ const TreeOrAccT& mAcc;

public:
    using ValueT = typename TreeOrAccT::ValueType;
    using CoordT = typename TreeOrAccT::CoordType;
    static __constant__ const int ORDER = 1;

    /// @brief Protected constructor from a Tree or ReadAccessor
    __hostdev__ TriquadraticSampler(__local__ const TreeOrAccT& acc) : mAcc(acc) {}

    __hostdev__ __global__ const TreeOrAccT& accessor() const { return mAcc; }

    /// @brief Extract the stencil of 27 values
    inline __hostdev__ void stencil(__local__ const CoordT &ijk, __local__ ValueT (&v)[3][3][3]) const;

    template<typename RealT, template<typename...> class Vec3T>
    static inline __hostdev__ ValueT sample(__local__ const Vec3T<RealT> &uvw, __local__ const ValueT (&v)[3][3][3]);

    static inline __hostdev__ bool zeroCrossing(__global__ const ValueT (&v)[3][3][3]);
}; // TriquadraticSamplerBase

template<typename TreeOrAccT>
void TriquadraticSampler<TreeOrAccT>::stencil(__local__ const CoordT &ijk, __local__ ValueT (&v)[3][3][3]) const
{
    CoordT p(ijk[0] - 1, 0, 0);
    for (int dx = 0; dx < 3; ++dx, ++p[0]) {
        p[1] = ijk[1] - 1;
        for (int dy = 0; dy < 3; ++dy, ++p[1]) {
            p[2] = ijk[2] - 1;
            for (int dz = 0; dz < 3; ++dz, ++p[2]) {
                v[dx][dy][dz] = mAcc.getValue(p);// extract the stencil of 27 values
            }
        }
    }
}

template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
typename TreeOrAccT::ValueType TriquadraticSampler<TreeOrAccT>::sample(__local__ const Vec3T<RealT> &uvw, __local__ const ValueT (&v)[3][3][3])
{
    struct Kernel {
        static ValueT _kernel(__local__ const ValueT* value, double weight) {
            return weight * (weight * (0.5f * (value[0] + value[2]) - value[1]) + 0.5f * (value[2] - value[0])) + value[1];
        }
    };

    ValueT vx[3];
    for (int dx = 0; dx < 3; ++dx) {
        ValueT vy[3];
        for (int dy = 0; dy < 3; ++dy) {
            vy[dy] = Kernel::_kernel(&v[dx][dy][0], uvw[2]);
        }//loop over y
        vx[dx] = Kernel::_kernel(vy, uvw[1]);
    }//loop over x
    return Kernel::_kernel(vx, uvw[0]);
}

template<typename TreeOrAccT>
bool TriquadraticSampler<TreeOrAccT>::zeroCrossing(__global__ const ValueT (&v)[3][3][3])
{
    static_assert(is_floating_point<ValueT>::value, "TrilinearSampler::zeroCrossing requires a floating-point type");
    const bool less = v[0][0][0] < ValueT(0);
    for (int dx = 0; dx < 3; ++dx) {
        for (int dy = 0; dy < 3; ++dy) {
            for (int dz = 0; dz < 3; ++dz) {
                if (less ^ (v[dx][dy][dz] < ValueT(0))) return true;
            }
        }
    }
    return false;
}

/// @brief Template specialization that does not use caching of stencil points
template<typename TreeOrAccT>
class SampleFromVoxels<TreeOrAccT, 2, false>
#if !defined(__KERNEL_METAL__)
    : public TriquadraticSampler<TreeOrAccT>
#endif
{
#if defined(__KERNEL_METAL__)
    TriquadraticSampler<TreeOrAccT> _base;
#define BASE(v) _base.v
#else
#define BASE(v) BaseT::v
#endif
    using BaseT = TriquadraticSampler<TreeOrAccT>;
    using ValueT = typename TreeOrAccT::ValueType;
    using CoordT = typename TreeOrAccT::CoordType;
public:

    /// @brief Construction from a Tree or ReadAccessor
#if defined(__KERNEL_METAL__)
    __hostdev__ SampleFromVoxels(__local__ const TreeOrAccT& acc) : _base(acc) {}
#else
    __hostdev__ SampleFromVoxels(__local__ const TreeOrAccT& acc) : BaseT(acc) {}
#endif

    /// @note xyz is in index space space
    template<typename RealT, template<typename...> class Vec3T>
    inline __hostdev__ ValueT operator()(Vec3T<RealT> xyz) const;

    __hostdev__ ValueT operator()(__global__ const CoordT &ijk) const {return BaseT::mAcc.getValue(ijk);}

    /// @brief Return true if the tr-linear stencil has a zero crossing at the specified index position.
    ///
    /// @warning Will only compile with floating point value types
    template<typename RealT, template<typename...> class Vec3T>
    inline __hostdev__ bool zeroCrossing(Vec3T<RealT> xyz) const;

}; // SampleFromVoxels<TreeOrAccT, 2, false>

/// @brief Template specialization with caching of stencil values
template<typename TreeOrAccT>
class SampleFromVoxels<TreeOrAccT, 2, true>
#if !defined(__KERNEL_METAL__)
    : public TriquadraticSampler<TreeOrAccT>
#endif
{
#if defined(__KERNEL_METAL__)
    TriquadraticSampler<TreeOrAccT> _base;
#define BASE(v) _base.v
#else
#define BASE(v) BaseT::v
#endif
    using BaseT = TriquadraticSampler<TreeOrAccT>;
    using ValueT = typename TreeOrAccT::ValueType;
    using CoordT = typename TreeOrAccT::CoordType;

    mutable CoordT mPos;
    mutable ValueT mVal[3][3][3];

    template<typename RealT, template<typename...> class Vec3T>
    __hostdev__ void cache(__global__ Vec3T<RealT>& xyz) const;
public:

    /// @brief Construction from a Tree or ReadAccessor
    __hostdev__ SampleFromVoxels(__local__ const TreeOrAccT& acc) : BaseT(acc), mPos(CoordT::max()){}

    /// @note xyz is in index space space
    template<typename RealT, template<typename...> class Vec3T>
    inline __hostdev__ ValueT operator()(Vec3T<RealT> xyz) const;

    inline __hostdev__ ValueT operator()(__global__ const CoordT &ijk) const;

    /// @brief Return true if the tr-linear stencil has a zero crossing at the specified index position.
    ///
    /// @warning Will only compile with floating point value types
    template<typename RealT, template<typename...> class Vec3T>
    inline __hostdev__ bool zeroCrossing(Vec3T<RealT> xyz) const;

    /// @brief Return true if the cached tri-linear stencil has a zero crossing.
    ///
    /// @warning Will only compile with floating point value types
    __hostdev__ bool zeroCrossing() const { return BaseT::zeroCrossing(mVal); }

}; // SampleFromVoxels<TreeOrAccT, 2, true>

template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
typename TreeOrAccT::ValueType SampleFromVoxels<TreeOrAccT, 2, true>::operator()(Vec3T<RealT> xyz) const
{
    this->cache(xyz);
    return BaseT::sample(xyz, mVal);
}

template<typename TreeOrAccT>
typename TreeOrAccT::ValueType SampleFromVoxels<TreeOrAccT, 2, true>::operator()(__global__ const CoordT &ijk) const
{
    return  ijk == mPos ? mVal[1][1][1] : BaseT::mAcc.getValue(ijk);
}

template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
__hostdev__ bool SampleFromVoxels<TreeOrAccT, 2, true>::zeroCrossing(Vec3T<RealT> xyz) const
{
    this->cache(xyz);
    return BaseT::zeroCrossing(mVal);
}

template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
void SampleFromVoxels<TreeOrAccT, 2, true>::cache(__global__ Vec3T<RealT>& xyz) const
{
    CoordT ijk = Floor<CoordT>(xyz);
    if (ijk != mPos) {
        mPos = ijk;
        BaseT::stencil(ijk, mVal);
    }
}

template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
typename TreeOrAccT::ValueType SampleFromVoxels<TreeOrAccT, 2, false>::operator()(Vec3T<RealT> xyz) const
{
    ValueT val[3][3][3];
    CoordT ijk = Floor<CoordT>(xyz);
    BASE(stencil)(ijk, val);
    return BaseT::sample(xyz, val);
}

template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
bool SampleFromVoxels<TreeOrAccT, 2, false>::zeroCrossing(Vec3T<RealT> xyz) const
{
    ValueT val[3][3][3];
    CoordT ijk = Floor<CoordT>(xyz);
    BaseT::stencil(ijk, val);
    return BaseT::zeroCrossing(val);
}

// ------------------------------> TricubicSampler <--------------------------------------

/// @brief Tri-cubic sampler, i.e. third order, interpolator.
///
/// @details See the following paper for implementation details:
/// Lekien, F. and Marsden, J.: Tricubic interpolation in three dimensions.
///                         In: International Journal for Numerical Methods
///                         in Engineering (2005), No. 63, p. 455-471

template<typename TreeOrAccT>
class TricubicSampler
{
protected:
    using ValueT = typename TreeOrAccT::ValueType;
    using CoordT = typename TreeOrAccT::CoordType;

    __global__ const TreeOrAccT& mAcc;

public:
    /// @brief Construction from a Tree or ReadAccessor
    __hostdev__ TricubicSampler(__global__ const TreeOrAccT& acc)
        : mAcc(acc)
    {
    }

    __hostdev__ __global__ const TreeOrAccT& accessor() const { return mAcc; }

     /// @brief Extract the stencil of 8 values
    inline __hostdev__ void stencil(__global__ const CoordT& ijk, __global__ ValueT (&c)[64]) const;

    template<typename RealT, template<typename...> class Vec3T>
    static inline __hostdev__ ValueT sample(__global__ const Vec3T<RealT> &uvw, __global__ const ValueT (&c)[64]);
}; // TricubicSampler

// 4Kb of static table (int8_t has a range of -127 -> 127 which suffices)
static __constant__ const int8_t TricubicSampler_A[64][64] = {
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {-3, 3, 0, 0, 0, 0, 0, 0, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {2, -2, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {-3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {9, -9, -9, 9, 0, 0, 0, 0, 6, 3, -6, -3, 0, 0, 0, 0, 6, -6, 3, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {-6, 6, 6, -6, 0, 0, 0, 0, -3, -3, 3, 3, 0, 0, 0, 0, -4, 4, -2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, -2, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {2, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 2, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {-6, 6, 6, -6, 0, 0, 0, 0, -4, -2, 4, 2, 0, 0, 0, 0, -3, 3, -3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, -1, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {4, -4, -4, 4, 0, 0, 0, 0, 2, 2, -2, -2, 0, 0, 0, 0, 2, -2, 2, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 3, 0, 0, 0, 0, 0, 0, -2, -1, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, -2, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, -1, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, -9, -9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, -6, -3, 0, 0, 0, 0, 6, -6, 3, -3, 0, 0, 0, 0, 4, 2, 2, 1, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -6, 6, 6, -6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, -3, 3, 3, 0, 0, 0, 0, -4, 4, -2, 2, 0, 0, 0, 0, -2, -2, -1, -1, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -6, 6, 6, -6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4, -2, 4, 2, 0, 0, 0, 0, -3, 3, -3, 3, 0, 0, 0, 0, -2, -1, -2, -1, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, -4, -4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, -2, -2, 0, 0, 0, 0, 2, -2, 2, -2, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0},
    {-3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {9, -9, 0, 0, -9, 9, 0, 0, 6, 3, 0, 0, -6, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, -6, 0, 0, 3, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {-6, 6, 0, 0, 6, -6, 0, 0, -3, -3, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4, 4, 0, 0, -2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, -2, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, -1, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, -9, 0, 0, -9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 0, 0, -6, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, -6, 0, 0, 3, -3, 0, 0, 4, 2, 0, 0, 2, 1, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -6, 6, 0, 0, 6, -6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, -3, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4, 4, 0, 0, -2, 2, 0, 0, -2, -2, 0, 0, -1, -1, 0, 0},
    {9, 0, -9, 0, -9, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 3, 0, -6, 0, -3, 0, 6, 0, -6, 0, 3, 0, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 9, 0, -9, 0, -9, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 3, 0, -6, 0, -3, 0, 6, 0, -6, 0, 3, 0, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 2, 0, 2, 0, 1, 0},
    {-27, 27, 27, -27, 27, -27, -27, 27, -18, -9, 18, 9, 18, 9, -18, -9, -18, 18, -9, 9, 18, -18, 9, -9, -18, 18, 18, -18, -9, 9, 9, -9, -12, -6, -6, -3, 12, 6, 6, 3, -12, -6, 12, 6, -6, -3, 6, 3, -12, 12, -6, 6, -6, 6, -3, 3, -8, -4, -4, -2, -4, -2, -2, -1},
    {18, -18, -18, 18, -18, 18, 18, -18, 9, 9, -9, -9, -9, -9, 9, 9, 12, -12, 6, -6, -12, 12, -6, 6, 12, -12, -12, 12, 6, -6, -6, 6, 6, 6, 3, 3, -6, -6, -3, -3, 6, 6, -6, -6, 3, 3, -3, -3, 8, -8, 4, -4, 4, -4, 2, -2, 4, 4, 2, 2, 2, 2, 1, 1},
    {-6, 0, 6, 0, 6, 0, -6, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, -3, 0, 3, 0, 3, 0, -4, 0, 4, 0, -2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, -2, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, -6, 0, 6, 0, 6, 0, -6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, -3, 0, 3, 0, 3, 0, -4, 0, 4, 0, -2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, -2, 0, -1, 0, -1, 0},
    {18, -18, -18, 18, -18, 18, 18, -18, 12, 6, -12, -6, -12, -6, 12, 6, 9, -9, 9, -9, -9, 9, -9, 9, 12, -12, -12, 12, 6, -6, -6, 6, 6, 3, 6, 3, -6, -3, -6, -3, 8, 4, -8, -4, 4, 2, -4, -2, 6, -6, 6, -6, 3, -3, 3, -3, 4, 2, 4, 2, 2, 1, 2, 1},
    {-12, 12, 12, -12, 12, -12, -12, 12, -6, -6, 6, 6, 6, 6, -6, -6, -6, 6, -6, 6, 6, -6, 6, -6, -8, 8, 8, -8, -4, 4, 4, -4, -3, -3, -3, -3, 3, 3, 3, 3, -4, -4, 4, 4, -2, -2, 2, 2, -4, 4, -4, 4, -2, 2, -2, 2, -2, -2, -2, -2, -1, -1, -1, -1},
    {2, 0, 0, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {-6, 6, 0, 0, 6, -6, 0, 0, -4, -2, 0, 0, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 3, 0, 0, -3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, -1, 0, 0, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {4, -4, 0, 0, -4, 4, 0, 0, 2, 2, 0, 0, -2, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, -2, 0, 0, 2, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -6, 6, 0, 0, 6, -6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4, -2, 0, 0, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 3, 0, 0, -3, 3, 0, 0, -2, -1, 0, 0, -2, -1, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, -4, 0, 0, -4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, -2, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, -2, 0, 0, 2, -2, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0},
    {-6, 0, 6, 0, 6, 0, -6, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4, 0, -2, 0, 4, 0, 2, 0, -3, 0, 3, 0, -3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, -1, 0, -2, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, -6, 0, 6, 0, 6, 0, -6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4, 0, -2, 0, 4, 0, 2, 0, -3, 0, 3, 0, -3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, -1, 0, -2, 0, -1, 0},
    {18, -18, -18, 18, -18, 18, 18, -18, 12, 6, -12, -6, -12, -6, 12, 6, 12, -12, 6, -6, -12, 12, -6, 6, 9, -9, -9, 9, 9, -9, -9, 9, 8, 4, 4, 2, -8, -4, -4, -2, 6, 3, -6, -3, 6, 3, -6, -3, 6, -6, 3, -3, 6, -6, 3, -3, 4, 2, 2, 1, 4, 2, 2, 1},
    {-12, 12, 12, -12, 12, -12, -12, 12, -6, -6, 6, 6, 6, 6, -6, -6, -8, 8, -4, 4, 8, -8, 4, -4, -6, 6, 6, -6, -6, 6, 6, -6, -4, -4, -2, -2, 4, 4, 2, 2, -3, -3, 3, 3, -3, -3, 3, 3, -4, 4, -2, 2, -4, 4, -2, 2, -2, -2, -1, -1, -2, -2, -1, -1},
    {4, 0, -4, 0, -4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, -2, 0, -2, 0, 2, 0, -2, 0, 2, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 4, 0, -4, 0, -4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, -2, 0, -2, 0, 2, 0, -2, 0, 2, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0},
    {-12, 12, 12, -12, 12, -12, -12, 12, -8, -4, 8, 4, 8, 4, -8, -4, -6, 6, -6, 6, 6, -6, 6, -6, -6, 6, 6, -6, -6, 6, 6, -6, -4, -2, -4, -2, 4, 2, 4, 2, -4, -2, 4, 2, -4, -2, 4, 2, -3, 3, -3, 3, -3, 3, -3, 3, -2, -1, -2, -1, -2, -1, -2, -1},
    {8, -8, -8, 8, -8, 8, 8, -8, 4, 4, -4, -4, -4, -4, 4, 4, 4, -4, 4, -4, -4, 4, -4, 4, 4, -4, -4, 4, 4, -4, -4, 4, 2, 2, 2, 2, -2, -2, -2, -2, 2, 2, -2, -2, 2, 2, -2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 1, 1, 1, 1, 1, 1, 1, 1}};

template<typename TreeOrAccT>
void TricubicSampler<TreeOrAccT>::stencil(__global__ const CoordT& ijk, __global__ ValueT (&C)[64]) const
{
    struct Fetch {
        Fetch(__global__ ValueT (&_C)[64]):C(_C) {}
        __global__ ValueT& fetch(int i, int j, int k) { return C[((i + 1) << 4) + ((j + 1) << 2) + k + 1]; }

        __global__ ValueT (&C)[64];
    };
    Fetch f(C);

    // fetch 64 point stencil values
    for (int i = -1; i < 3; ++i) {
        for (int j = -1; j < 3; ++j) {
            Fetch::fetch(i, j, -1) = mAcc.getValue(ijk + CoordT(i, j, -1));
            Fetch::fetch(i, j,  0) = mAcc.getValue(ijk + CoordT(i, j,  0));
            Fetch::fetch(i, j,  1) = mAcc.getValue(ijk + CoordT(i, j,  1));
            Fetch::fetch(i, j,  2) = mAcc.getValue(ijk + CoordT(i, j,  2));
        }
    }
    const ValueT _half(0.5), quarter(0.25), eighth(0.125);
    const ValueT X[64] = {// values of f(x,y,z) at the 8 corners (each from 1 stencil value).
                          f.fetch(0, 0, 0),
                          f.fetch(1, 0, 0),
                          f.fetch(0, 1, 0),
                          f.fetch(1, 1, 0),
                          f.fetch(0, 0, 1),
                          f.fetch(1, 0, 1),
                          f.fetch(0, 1, 1),
                          f.fetch(1, 1, 1),
                          // values of df/dx at the 8 corners (each from 2 stencil values).
                          _half * (f.fetch(1, 0, 0) - f.fetch(-1, 0, 0)),
                          _half * (f.fetch(2, 0, 0) - f.fetch(0, 0, 0)),
                          _half * (f.fetch(1, 1, 0) - f.fetch(-1, 1, 0)),
                          _half * (f.fetch(2, 1, 0) - f.fetch(0, 1, 0)),
                          _half * (f.fetch(1, 0, 1) - f.fetch(-1, 0, 1)),
                          _half * (f.fetch(2, 0, 1) - f.fetch(0, 0, 1)),
                          _half * (f.fetch(1, 1, 1) - f.fetch(-1, 1, 1)),
                          _half * (f.fetch(2, 1, 1) - f.fetch(0, 1, 1)),
                          // values of df/dy at the 8 corners (each from 2 stencil values).
                          _half * (f.fetch(0, 1, 0) - f.fetch(0, -1, 0)),
                          _half * (f.fetch(1, 1, 0) - f.fetch(1, -1, 0)),
                          _half * (f.fetch(0, 2, 0) - f.fetch(0, 0, 0)),
                          _half * (f.fetch(1, 2, 0) - f.fetch(1, 0, 0)),
                          _half * (f.fetch(0, 1, 1) - f.fetch(0, -1, 1)),
                          _half * (f.fetch(1, 1, 1) - f.fetch(1, -1, 1)),
                          _half * (f.fetch(0, 2, 1) - f.fetch(0, 0, 1)),
                          _half * (f.fetch(1, 2, 1) - f.fetch(1, 0, 1)),
                          // values of df/dz at the 8 corners (each from 2 stencil values).
                          _half * (f.fetch(0, 0, 1) - f.fetch(0, 0, -1)),
                          _half * (f.fetch(1, 0, 1) - f.fetch(1, 0, -1)),
                          _half * (f.fetch(0, 1, 1) - f.fetch(0, 1, -1)),
                          _half * (f.fetch(1, 1, 1) - f.fetch(1, 1, -1)),
                          _half * (f.fetch(0, 0, 2) - f.fetch(0, 0, 0)),
                          _half * (f.fetch(1, 0, 2) - f.fetch(1, 0, 0)),
                          _half * (f.fetch(0, 1, 2) - f.fetch(0, 1, 0)),
                          _half * (f.fetch(1, 1, 2) - f.fetch(1, 1, 0)),
                          // values of d2f/dxdy at the 8 corners (each from 4 stencil values).
                          quarter * (f.fetch(1, 1, 0) - f.fetch(-1, 1, 0) - f.fetch(1, -1, 0) + f.fetch(-1, -1, 0)),
                          quarter * (f.fetch(2, 1, 0) - f.fetch(0, 1, 0) - f.fetch(2, -1, 0) + f.fetch(0, -1, 0)),
                          quarter * (f.fetch(1, 2, 0) - f.fetch(-1, 2, 0) - f.fetch(1, 0, 0) + f.fetch(-1, 0, 0)),
                          quarter * (f.fetch(2, 2, 0) - f.fetch(0, 2, 0) - f.fetch(2, 0, 0) + f.fetch(0, 0, 0)),
                          quarter * (f.fetch(1, 1, 1) - f.fetch(-1, 1, 1) - f.fetch(1, -1, 1) + f.fetch(-1, -1, 1)),
                          quarter * (f.fetch(2, 1, 1) - f.fetch(0, 1, 1) - f.fetch(2, -1, 1) + f.fetch(0, -1, 1)),
                          quarter * (f.fetch(1, 2, 1) - f.fetch(-1, 2, 1) - f.fetch(1, 0, 1) + f.fetch(-1, 0, 1)),
                          quarter * (f.fetch(2, 2, 1) - f.fetch(0, 2, 1) - f.fetch(2, 0, 1) + f.fetch(0, 0, 1)),
                          // values of d2f/dxdz at the 8 corners (each from 4 stencil values).
                          quarter * (f.fetch(1, 0, 1) - f.fetch(-1, 0, 1) - f.fetch(1, 0, -1) + f.fetch(-1, 0, -1)),
                          quarter * (f.fetch(2, 0, 1) - f.fetch(0, 0, 1) - f.fetch(2, 0, -1) + f.fetch(0, 0, -1)),
                          quarter * (f.fetch(1, 1, 1) - f.fetch(-1, 1, 1) - f.fetch(1, 1, -1) + f.fetch(-1, 1, -1)),
                          quarter * (f.fetch(2, 1, 1) - f.fetch(0, 1, 1) - f.fetch(2, 1, -1) + f.fetch(0, 1, -1)),
                          quarter * (f.fetch(1, 0, 2) - f.fetch(-1, 0, 2) - f.fetch(1, 0, 0) + f.fetch(-1, 0, 0)),
                          quarter * (f.fetch(2, 0, 2) - f.fetch(0, 0, 2) - f.fetch(2, 0, 0) + f.fetch(0, 0, 0)),
                          quarter * (f.fetch(1, 1, 2) - f.fetch(-1, 1, 2) - f.fetch(1, 1, 0) + f.fetch(-1, 1, 0)),
                          quarter * (f.fetch(2, 1, 2) - f.fetch(0, 1, 2) - f.fetch(2, 1, 0) + f.fetch(0, 1, 0)),
                          // values of d2f/dydz at the 8 corners (each from 4 stencil values).
                          quarter * (f.fetch(0, 1, 1) - f.fetch(0, -1, 1) - f.fetch(0, 1, -1) + f.fetch(0, -1, -1)),
                          quarter * (f.fetch(1, 1, 1) - f.fetch(1, -1, 1) - f.fetch(1, 1, -1) + f.fetch(1, -1, -1)),
                          quarter * (f.fetch(0, 2, 1) - f.fetch(0, 0, 1) - f.fetch(0, 2, -1) + f.fetch(0, 0, -1)),
                          quarter * (f.fetch(1, 2, 1) - f.fetch(1, 0, 1) - f.fetch(1, 2, -1) + f.fetch(1, 0, -1)),
                          quarter * (f.fetch(0, 1, 2) - f.fetch(0, -1, 2) - f.fetch(0, 1, 0) + f.fetch(0, -1, 0)),
                          quarter * (f.fetch(1, 1, 2) - f.fetch(1, -1, 2) - f.fetch(1, 1, 0) + f.fetch(1, -1, 0)),
                          quarter * (f.fetch(0, 2, 2) - f.fetch(0, 0, 2) - f.fetch(0, 2, 0) + f.fetch(0, 0, 0)),
                          quarter * (f.fetch(1, 2, 2) - f.fetch(1, 0, 2) - f.fetch(1, 2, 0) + f.fetch(1, 0, 0)),
                          // values of d3f/dxdydz at the 8 corners (each from 8 stencil values).
                          eighth * (f.fetch(1, 1, 1) - f.fetch(-1, 1, 1) - f.fetch(1, -1, 1) + f.fetch(-1, -1, 1) - f.fetch(1, 1, -1) + f.fetch(-1, 1, -1) + f.fetch(1, -1, -1) - f.fetch(-1, -1, -1)),
                          eighth * (f.fetch(2, 1, 1) - f.fetch(0, 1, 1) - f.fetch(2, -1, 1) + f.fetch(0, -1, 1) - f.fetch(2, 1, -1) + f.fetch(0, 1, -1) + f.fetch(2, -1, -1) - f.fetch(0, -1, -1)),
                          eighth * (f.fetch(1, 2, 1) - f.fetch(-1, 2, 1) - f.fetch(1, 0, 1) + f.fetch(-1, 0, 1) - f.fetch(1, 2, -1) + f.fetch(-1, 2, -1) + f.fetch(1, 0, -1) - f.fetch(-1, 0, -1)),
                          eighth * (f.fetch(2, 2, 1) - f.fetch(0, 2, 1) - f.fetch(2, 0, 1) + f.fetch(0, 0, 1) - f.fetch(2, 2, -1) + f.fetch(0, 2, -1) + f.fetch(2, 0, -1) - f.fetch(0, 0, -1)),
                          eighth * (f.fetch(1, 1, 2) - f.fetch(-1, 1, 2) - f.fetch(1, -1, 2) + f.fetch(-1, -1, 2) - f.fetch(1, 1, 0) + f.fetch(-1, 1, 0) + f.fetch(1, -1, 0) - f.fetch(-1, -1, 0)),
                          eighth * (f.fetch(2, 1, 2) - f.fetch(0, 1, 2) - f.fetch(2, -1, 2) + f.fetch(0, -1, 2) - f.fetch(2, 1, 0) + f.fetch(0, 1, 0) + f.fetch(2, -1, 0) - f.fetch(0, -1, 0)),
                          eighth * (f.fetch(1, 2, 2) - f.fetch(-1, 2, 2) - f.fetch(1, 0, 2) + f.fetch(-1, 0, 2) - f.fetch(1, 2, 0) + f.fetch(-1, 2, 0) + f.fetch(1, 0, 0) - f.fetch(-1, 0, 0)),
                          eighth * (f.fetch(2, 2, 2) - f.fetch(0, 2, 2) - f.fetch(2, 0, 2) + f.fetch(0, 0, 2) - f.fetch(2, 2, 0) + f.fetch(0, 2, 0) + f.fetch(2, 0, 0) - f.fetch(0, 0, 0))};

    for (int i = 0; i < 64; ++i) { // C = A * X
        C[i] = ValueT(0);
#if 0
    for (int j = 0; j < 64; j += 4) {
      C[i] = fma(A[i][j], X[j], fma(A[i][j+1], X[j+1], fma(A[i][j+2], X[j+2], fma(A[i][j+3], X[j+3], C[i]))));
    }
#else
        for (int j = 0; j < 64; j += 4) {
            C[i] += TricubicSampler_A[i][j] * X[j] + TricubicSampler_A[i][j + 1] * X[j + 1] +
                    TricubicSampler_A[i][j + 2] * X[j + 2] + TricubicSampler_A[i][j + 3] * X[j + 3];
        }
#endif
    }
}

template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
__hostdev__ typename TreeOrAccT::ValueType TricubicSampler<TreeOrAccT>::sample(__global__ const Vec3T<RealT> &xyz, __global__ const ValueT (&C)[64])
{
    ValueT zPow(1), sum(0);
    for (int k = 0, n = 0; k < 4; ++k) {
        ValueT yPow(1);
        for (int j = 0; j < 4; ++j, n += 4) {
#if 0
            sum = fma( yPow, zPow * fma(xyz[0], fma(xyz[0], fma(xyz[0], C[n + 3], C[n + 2]), C[n + 1]), C[n]), sum);
#else
            sum += yPow * zPow * (C[n] + xyz[0] * (C[n + 1] + xyz[0] * (C[n + 2] + xyz[0] * C[n + 3])));
#endif
            yPow *= xyz[1];
        }
        zPow *= xyz[2];
    }
    return sum;
}

template<typename TreeOrAccT>
class SampleFromVoxels<TreeOrAccT, 3, true>
#if !defined(__KERNEL_METAL__)
    : public TricubicSampler<TreeOrAccT>
#endif
{
#if defined(__KERNEL_METAL__)
    TricubicSampler<TreeOrAccT> _base;
#define BASE(v) _base.v
#else
#define BASE(v) BaseT::v
#endif
    using BaseT  = TricubicSampler<TreeOrAccT>;
    using ValueT = typename TreeOrAccT::ValueType;
    using CoordT = typename TreeOrAccT::CoordType;

    mutable CoordT mPos;
    mutable ValueT mC[64];

    template<typename RealT, template<typename...> class Vec3T>
    __hostdev__ void cache(__global__ Vec3T<RealT>& xyz) const;

public:
    /// @brief Construction from a Tree or ReadAccessor
    __hostdev__ SampleFromVoxels(__local__ const TreeOrAccT& acc)
        : BaseT(acc)
    {
    }

    /// @note xyz is in index space space
    template<typename RealT, template<typename...> class Vec3T>
    inline __hostdev__ ValueT operator()(Vec3T<RealT> xyz) const;

    // @brief Return value at the coordinate @a ijk in index space space
    __hostdev__ ValueT operator()(__global__ const CoordT &ijk) const {return BaseT::mAcc.getValue(ijk);}

}; // SampleFromVoxels<TreeOrAccT, 3, true>

template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
typename TreeOrAccT::ValueType SampleFromVoxels<TreeOrAccT, 3, true>::operator()(Vec3T<RealT> xyz) const
{
    this->cache(xyz);
    return BaseT::sample(xyz, mC);
}

template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
void SampleFromVoxels<TreeOrAccT, 3, true>::cache(__global__ Vec3T<RealT>& xyz) const
{
    CoordT ijk = Floor<CoordT>(xyz);
    if (ijk != mPos) {
        mPos = ijk;
        BaseT::stencil(ijk, mC);
    }
}

template<typename TreeOrAccT>
class SampleFromVoxels<TreeOrAccT, 3, false>
#if !defined(__KERNEL_METAL__)
    : public TricubicSampler<TreeOrAccT>
#endif
{
#if defined(__KERNEL_METAL__)
    TricubicSampler<TreeOrAccT> _base;
#define BASE(v) _base.v
#else
#define BASE(v) BaseT::v
#endif
    using BaseT  = TricubicSampler<TreeOrAccT>;
    using ValueT = typename TreeOrAccT::ValueType;
    using CoordT = typename TreeOrAccT::CoordType;

public:
    /// @brief Construction from a Tree or ReadAccessor
    __hostdev__ SampleFromVoxels(__local__ const TreeOrAccT& acc)
        : BaseT(acc)
    {
    }

    /// @note xyz is in index space space
    template<typename RealT, template<typename...> class Vec3T>
    inline __hostdev__ ValueT operator()(Vec3T<RealT> xyz) const;

    __hostdev__ ValueT operator()(__global__ const CoordT &ijk) const {return BaseT::mAcc.getValue(ijk);}

}; // SampleFromVoxels<TreeOrAccT, 3, true>

template<typename TreeOrAccT>
template<typename RealT, template<typename...> class Vec3T>
__hostdev__ typename TreeOrAccT::ValueType SampleFromVoxels<TreeOrAccT, 3, false>::operator()(Vec3T<RealT> xyz) const
{
    ValueT C[64];
    CoordT ijk = Floor<CoordT>(xyz);
    BaseT::stencil(ijk, C);
    return BaseT::sample(xyz, C);
}

} // namespace nanovdb

#endif // NANOVDB_SAMPLE_FROM_VOXELS_H_HAS_BEEN_INCLUDED
